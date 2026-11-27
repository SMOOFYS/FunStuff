import type { Express } from "express";
import { createServer, type Server } from "http";
import { storage } from "./storage";
import { insertLocationSchema, insertLocationFileSchema, insertCompilationResultSchema } from "@shared/schema";
import { spawn } from "child_process";
import fs from "fs/promises";
import path from "path";
import multer from "multer";

// In-memory store for compiled binary directories (keyed by compilation ID)
const compiledBinaries = new Map<string, string>();

// Configure multer for file uploads
const upload = multer({
  storage: multer.memoryStorage(),
  limits: {
    fileSize: 1024 * 1024, // 1MB limit
  }
});

export async function registerRoutes(app: Express): Promise<Server> {
  // Location routes
  app.get("/api/locations", async (req, res) => {
    try {
      const locations = await storage.getAllLocations();
      res.json(locations);
    } catch (error) {
      res.status(500).json({ message: "Failed to fetch locations" });
    }
  });

  app.post("/api/locations", async (req, res) => {
    try {
      const locationData = insertLocationSchema.parse(req.body);
      const location = await storage.createLocation(locationData);
      res.json(location);
    } catch (error) {
      res.status(400).json({ message: "Invalid location data" });
    }
  });

  app.delete("/api/locations/:id", async (req, res) => {
    try {
      const success = await storage.deleteLocation(req.params.id);
      if (success) {
        res.json({ message: "Location deleted successfully" });
      } else {
        res.status(404).json({ message: "Location not found" });
      }
    } catch (error) {
      res.status(500).json({ message: "Failed to delete location" });
    }
  });

  app.delete("/api/locations", async (req, res) => {
    try {
      await storage.clearAllLocations();
      res.json({ message: "All locations cleared successfully" });
    } catch (error) {
      res.status(500).json({ message: "Failed to clear locations" });
    }
  });

  // Distance calculation route
  app.post("/api/locations/distance", async (req, res) => {
    try {
      const { location1Id, location2Id } = req.body;
      const loc1 = await storage.getLocation(location1Id);
      const loc2 = await storage.getLocation(location2Id);
      
      if (!loc1 || !loc2) {
        return res.status(404).json({ message: "One or both locations not found" });
      }

      // Calculate Euclidean distance
      const distance = Math.sqrt(Math.pow(loc1.x - loc2.x, 2) + Math.pow(loc1.y - loc2.y, 2));
      
      res.json({ distance: parseFloat(distance.toFixed(2)) });
    } catch (error) {
      res.status(500).json({ message: "Failed to calculate distance" });
    }
  });

  // File upload and processing routes
  app.post("/api/files/upload", upload.single('file'), async (req, res) => {
    try {
      if (!req.file) {
        return res.status(400).json({ message: "No file uploaded" });
      }

      const content = req.file.buffer.toString('utf-8');
      const filename = req.file.originalname;

      // Validate file format (should be space-separated x y coordinates)
      const lines = content.trim().split('\n');
      const locations: { x: number; y: number }[] = [];
      
      for (let i = 0; i < lines.length; i++) {
        const line = lines[i].trim();
        if (!line) continue;
        
        const parts = line.split(/\s+/);
        if (parts.length !== 2) {
          return res.status(400).json({ 
            message: `Invalid format at line ${i + 1}. Expected: "x y"` 
          });
        }
        
        const x = parseInt(parts[0]);
        const y = parseInt(parts[1]);
        
        if (isNaN(x) || isNaN(y)) {
          return res.status(400).json({ 
            message: `Invalid coordinates at line ${i + 1}. Must be integers.` 
          });
        }
        
        locations.push({ x, y });
      }

      // Store the file
      const file = await storage.createLocationFile({ filename, content });

      // Create location objects
      const createdLocations = [];
      for (const loc of locations) {
        const location = await storage.createLocation(loc);
        createdLocations.push(location);
      }

      res.json({
        file,
        locations: createdLocations,
        message: `Successfully imported ${createdLocations.length} locations`
      });
    } catch (error) {
      res.status(500).json({ message: "Failed to process file" });
    }
  });

  app.get("/api/files", async (req, res) => {
    try {
      const files = await storage.getAllLocationFiles();
      res.json(files);
    } catch (error) {
      res.status(500).json({ message: "Failed to fetch files" });
    }
  });

  // C++ Compilation and execution routes
  app.post("/api/compile", async (req, res) => {
    try {
      const { sourceCode, compileOptions = [] } = req.body;
      
      if (!sourceCode) {
        return res.status(400).json({ message: "Source code is required" });
      }

      // Create temporary directory for compilation
      const tempDir = path.join(process.cwd(), 'temp', Date.now().toString());
      await fs.mkdir(tempDir, { recursive: true });

      // Write source files
      const mainFile = path.join(tempDir, 'main.cpp');
      await fs.writeFile(mainFile, sourceCode);

      // Copy header files from attached assets
      const headerFiles = ['LocationHeader.h', 'LocationFromFile.h'];
      const sourceFiles = ['Location.cpp', 'LocationFromFile.cpp'];
      
      for (const headerFile of headerFiles) {
        const headerPath = path.join(process.cwd(), 'attached_assets', headerFile.replace('.h', '_1758433388607.h'));
        const destPath = path.join(tempDir, headerFile);
        try {
          const content = await fs.readFile(headerPath, 'utf-8');
          await fs.writeFile(destPath, content);
        } catch (error) {
          // If header files don't exist, create minimal versions
          if (headerFile === 'LocationHeader.h') {
            await fs.writeFile(destPath, `
#ifndef __LOCATION_HEADER_H__
#define __LOCATION_HEADER_H__
#include <string>
using std::string;
class Location{
private: 
  int x, y;
public:
  static int count;
  Location();
  Location(int argx, int argy);
  double getDistance(Location other) const;
  Location create(int posX, int posY);
  Location create();
  string toString();
  int getX() { return x; }
  int getY() { return y; }
};
#endif
            `);
          } else if (headerFile === 'LocationFromFile.h') {
            await fs.writeFile(destPath, `
#ifndef __LOCATION_FROM_FILE_H__
#define __LOCATION_FROM_FILE_H__
#include <sstream>
#include <fstream>
#include <vector>
#include <iostream>
#include "LocationHeader.h"
using std::cout;
using std::vector;
void inputData(vector<Location> &vectorLocations, string fileName);
#endif
            `);
          }
        }
      }

      for (const sourceFile of sourceFiles) {
        const destPath = path.join(tempDir, sourceFile);
        let content = '';
        
        // Try multiple file path variations
        const possiblePaths = [
          path.join(process.cwd(), 'attached_assets', sourceFile), // Clean name first
          path.join(process.cwd(), 'attached_assets', sourceFile.replace('.cpp', '_1758433388605.cpp')), // Location timestamp
          path.join(process.cwd(), 'attached_assets', sourceFile.replace('.cpp', '_1758433388606.cpp'))  // LocationFromFile timestamp
        ];
        
        let fileFound = false;
        for (const possiblePath of possiblePaths) {
          try {
            content = await fs.readFile(possiblePath, 'utf-8');
            fileFound = true;
            break;
          } catch (error) {
            // Continue to next path
          }
        }
        
        if (!fileFound) {
          // Create minimal implementation if files don't exist
          if (sourceFile === 'Location.cpp') {
            content = `
#include <cmath>
#include "LocationHeader.h"
int Location::count = 0;
Location::Location() { x = 0; y = 0; count++; }
Location::Location(int otherX, int otherY) { x = otherX; y = otherY; count++; }
double Location::getDistance(Location other) const {
  return sqrt(pow(x - other.x, 2) + pow(y - other.y, 2));
}
Location Location::create(int posX, int posY) { return Location(posX, posY); }
Location Location::create() { return Location(); }
string Location::toString() { return "(" + std::to_string(x) + "," + std::to_string(y) + ")"; }
            `;
          } else if (sourceFile === 'LocationFromFile.cpp') {
            content = `
#include "LocationFromFile.h"
void inputData(vector<Location> &vectorLocations, string fileName){
  std::ifstream inFile;
  string info;
  int x, y;
  try {
    inFile.open(fileName);
    if (inFile.fail())
      throw string("File Open Error");
    while (!inFile.eof()) {
      getline(inFile, info);
      std::istringstream istream(info);
      istream >> x >> y;
      Location p(x, y);
      vectorLocations.push_back(p);
    }
  }
  catch( string msg ) {
    cout << msg;
    exit(0);
  }
}
            `;
          }
        }
        
        await fs.writeFile(destPath, content);
      }

      // Create LocationData.txt
      const dataFile = path.join(tempDir, 'LocationData.txt');
      const locations = await storage.getAllLocations();
      const locationData = locations.map(loc => `${loc.x} ${loc.y}`).join('\n');
      await fs.writeFile(dataFile, locationData);

      // Compile
      const outputFile = path.join(tempDir, 'program');
      const compileArgs = [
        '-o', outputFile,
        mainFile,
        ...sourceFiles.map(f => path.join(tempDir, f)),
        ...compileOptions
      ];

      const compileResult = await new Promise<{ success: boolean; output: string }>((resolve) => {
        const compiler = spawn('g++', compileArgs, { cwd: tempDir });
        let output = '';
        let errorOutput = '';

        compiler.stdout.on('data', (data) => {
          output += data.toString();
        });

        compiler.stderr.on('data', (data) => {
          errorOutput += data.toString();
        });

        compiler.on('close', (code) => {
          const fullOutput = output + errorOutput;
          resolve({
            success: code === 0,
            output: fullOutput || (code === 0 ? 'Compilation successful!' : 'Compilation failed')
          });
        });
      });

      // Store compilation result
      const result = await storage.createCompilationResult({
        sourceCode,
        compileOutput: compileResult.output,
        runOutput: '',
        success: compileResult.success ? 1 : 0
      });

      if (compileResult.success) {
        // Keep the temp directory so we can run the binary later
        compiledBinaries.set(result.id, tempDir);
      } else {
        // Clean up on failure
        await fs.rm(tempDir, { recursive: true, force: true });
      }

      res.json({
        ...result,
        success: compileResult.success
      });
    } catch (error) {
      res.status(500).json({ message: "Compilation failed: " + error });
    }
  });

  app.post("/api/run/:id", async (req, res) => {
    try {
      const compilationResult = await storage.getCompilationResult(req.params.id);
      
      if (!compilationResult || !compilationResult.success) {
        return res.status(404).json({ message: "No successful compilation found" });
      }

      const tempDir = compiledBinaries.get(req.params.id);
      if (!tempDir) {
        return res.status(404).json({ message: "Compiled binary not found. Please recompile." });
      }

      const binaryPath = path.join(tempDir, 'program');
      const stdinInput: string = req.body.stdin ?? "";

      const runResult = await new Promise<{ output: string; exitCode: number }>((resolve) => {
        const proc = spawn(binaryPath, [], { cwd: tempDir, timeout: 10000 });
        let output = '';

        proc.stdout.on('data', (data) => { output += data.toString(); });
        proc.stderr.on('data', (data) => { output += data.toString(); });

        proc.on('close', (code) => {
          resolve({ output, exitCode: code ?? 1 });
        });

        proc.on('error', (err) => {
          resolve({ output: `Error: ${err.message}`, exitCode: 1 });
        });

        // Write stdin then close it
        if (stdinInput) {
          proc.stdin.write(stdinInput);
        }
        proc.stdin.end();
      });

      // Clean up the temp directory after running
      compiledBinaries.delete(req.params.id);
      await fs.rm(tempDir, { recursive: true, force: true });

      res.json({
        output: runResult.output,
        exitCode: runResult.exitCode
      });
    } catch (error) {
      res.status(500).json({ message: "Execution failed: " + error });
    }
  });

  app.get("/api/compilations", async (req, res) => {
    try {
      const results = await storage.getAllCompilationResults();
      res.json(results);
    } catch (error) {
      res.status(500).json({ message: "Failed to fetch compilation results" });
    }
  });

  const httpServer = createServer(app);
  return httpServer;
}
