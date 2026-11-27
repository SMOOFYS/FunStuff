import { type User, type InsertUser, type Location, type InsertLocation, type LocationFile, type InsertLocationFile, type CompilationResult, type InsertCompilationResult } from "@shared/schema";
import { randomUUID } from "crypto";

export interface IStorage {
  getUser(id: string): Promise<User | undefined>;
  getUserByUsername(username: string): Promise<User | undefined>;
  createUser(user: InsertUser): Promise<User>;
  
  // Location operations
  getAllLocations(): Promise<Location[]>;
  getLocation(id: string): Promise<Location | undefined>;
  createLocation(location: InsertLocation): Promise<Location>;
  deleteLocation(id: string): Promise<boolean>;
  clearAllLocations(): Promise<void>;
  
  // File operations
  getAllLocationFiles(): Promise<LocationFile[]>;
  getLocationFile(id: string): Promise<LocationFile | undefined>;
  createLocationFile(file: InsertLocationFile): Promise<LocationFile>;
  deleteLocationFile(id: string): Promise<boolean>;
  
  // Compilation operations
  getAllCompilationResults(): Promise<CompilationResult[]>;
  getCompilationResult(id: string): Promise<CompilationResult | undefined>;
  createCompilationResult(result: InsertCompilationResult): Promise<CompilationResult>;
  deleteCompilationResult(id: string): Promise<boolean>;
}

export class MemStorage implements IStorage {
  private users: Map<string, User>;
  private locations: Map<string, Location>;
  private locationFiles: Map<string, LocationFile>;
  private compilationResults: Map<string, CompilationResult>;

  constructor() {
    this.users = new Map();
    this.locations = new Map();
    this.locationFiles = new Map();
    this.compilationResults = new Map();
  }

  async getUser(id: string): Promise<User | undefined> {
    return this.users.get(id);
  }

  async getUserByUsername(username: string): Promise<User | undefined> {
    return Array.from(this.users.values()).find(
      (user) => user.username === username,
    );
  }

  async createUser(insertUser: InsertUser): Promise<User> {
    const id = randomUUID();
    const user: User = { ...insertUser, id };
    this.users.set(id, user);
    return user;
  }

  // Location operations
  async getAllLocations(): Promise<Location[]> {
    return Array.from(this.locations.values()).sort((a, b) => 
      new Date(a.createdAt).getTime() - new Date(b.createdAt).getTime()
    );
  }

  async getLocation(id: string): Promise<Location | undefined> {
    return this.locations.get(id);
  }

  async createLocation(insertLocation: InsertLocation): Promise<Location> {
    const id = randomUUID();
    const location: Location = {
      ...insertLocation,
      id,
      createdAt: new Date(),
    };
    this.locations.set(id, location);
    return location;
  }

  async deleteLocation(id: string): Promise<boolean> {
    return this.locations.delete(id);
  }

  async clearAllLocations(): Promise<void> {
    this.locations.clear();
  }

  // File operations
  async getAllLocationFiles(): Promise<LocationFile[]> {
    return Array.from(this.locationFiles.values()).sort((a, b) => 
      new Date(b.processedAt).getTime() - new Date(a.processedAt).getTime()
    );
  }

  async getLocationFile(id: string): Promise<LocationFile | undefined> {
    return this.locationFiles.get(id);
  }

  async createLocationFile(insertFile: InsertLocationFile): Promise<LocationFile> {
    const id = randomUUID();
    const file: LocationFile = {
      ...insertFile,
      id,
      processedAt: new Date(),
    };
    this.locationFiles.set(id, file);
    return file;
  }

  async deleteLocationFile(id: string): Promise<boolean> {
    return this.locationFiles.delete(id);
  }

  // Compilation operations
  async getAllCompilationResults(): Promise<CompilationResult[]> {
    return Array.from(this.compilationResults.values()).sort((a, b) => 
      new Date(b.compiledAt).getTime() - new Date(a.compiledAt).getTime()
    );
  }

  async getCompilationResult(id: string): Promise<CompilationResult | undefined> {
    return this.compilationResults.get(id);
  }

  async createCompilationResult(insertResult: InsertCompilationResult): Promise<CompilationResult> {
    const id = randomUUID();
    const result: CompilationResult = {
      sourceCode: insertResult.sourceCode,
      compileOutput: insertResult.compileOutput ?? null,
      runOutput: insertResult.runOutput ?? null,
      success: insertResult.success ?? 0,
      id,
      compiledAt: new Date(),
    };
    this.compilationResults.set(id, result);
    return result;
  }

  async deleteCompilationResult(id: string): Promise<boolean> {
    return this.compilationResults.delete(id);
  }
}

export const storage = new MemStorage();
