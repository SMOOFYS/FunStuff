import { useState, useMemo } from "react";
import { useQuery, useMutation } from "@tanstack/react-query";
import { queryClient } from "@/lib/queryClient";
import { apiRequest } from "@/lib/queryClient";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Textarea } from "@/components/ui/textarea";
import { useToast } from "@/hooks/use-toast";
import { LocationPlot } from "@/components/location-plot";
import { FileUpload } from "@/components/file-upload";
import { TerminalOutput } from "@/components/terminal-output";
import { 
  Box, 
  Plus, 
  Upload, 
  ChartScatter, 
  Settings, 
  MapPin, 
  Calculator, 
  Trash2, 
  Download,
  Save,
  Home,
  Play,
  Code
} from "lucide-react";
import { Location } from "@shared/schema";

export default function HomePage() {
  const [activeTab, setActiveTab] = useState("create");
  const [newLocation, setNewLocation] = useState({ x: 0, y: 0 });
  const [selectedLocation1, setSelectedLocation1] = useState<string>("");
  const [selectedLocation2, setSelectedLocation2] = useState<string>("");
  const [sourceCode, setSourceCode] = useState(`#include <iostream>
#include <sstream>
#include <iomanip>
#include "LocationFromFile.h"

using namespace std;

void fillAndDisplay(Location * p[], const int numLocations) {
  for (int i = 0; i < numLocations; i++) {
    p[i] = new Location(i, i);
  }
  for (int i = 0; i < numLocations; i++) {
    cout << p[i]->toString() << endl;
  }
}

void emptyArray(Location *p[], const int numLocations) {
  for (int i = 0; i < numLocations; i++) {
    delete p[i];
  }
}

int main() {
  int x, y;
  cout << "Enter two integers, separated by a space, for the 1st location: ";
  cin >> x >> y;

  Location * pLocation1;
  Location p1(x,y);
  pLocation1 = &p1;
  cout << "First location: " << pLocation1->toString() << endl;

  cout << "Enter two integers, separated by a space, for the 2nd location: ";
  cin >> x >> y;
  Location * pLocation2 = new Location(x, y);
  cout << "Second location: " << pLocation2->toString() << endl;

  double distance = pLocation1->getDistance(*pLocation2);
  cout << fixed << std::setw(10) << std::setprecision(2);
  cout << "The distance between " << pLocation1->toString() << " and "
    << pLocation2->toString() << " is: " << distance << endl;
  cout << endl;
  delete pLocation2;

  const int numLocations = 6;
  cout << "Next " << numLocations << " locations: " << endl;
  Location * LocationArray[numLocations];
  fillAndDisplay(LocationArray, numLocations);
  cout << endl;
  emptyArray(LocationArray, numLocations);

  vector<Location> vLocations;
  inputData(vLocations, "LocationData.txt");
  int count = vLocations.size();
  cout << "Found " << count << " locations from file" << endl;
  cout << "They are :" << endl;
  for (int i = 0; i < count; i++)
    cout << vLocations[i].toString() << endl;

  int totalLocations = vLocations.back().count;
  cout << "\\nTotal locations: " << totalLocations << endl;

  return 0;
}`);
  const [stdinInput, setStdinInput] = useState("2 3\n0 0");
  const [terminalOutput, setTerminalOutput] = useState("");
  const [isCompiling, setIsCompiling] = useState(false);
  const [isRunning, setIsRunning] = useState(false);
  const [lastCompilationId, setLastCompilationId] = useState<string | null>(null);
  
  const { toast } = useToast();

  // Fetch locations
  const { data: locations = [], isLoading: locationsLoading } = useQuery<Location[]>({
    queryKey: ['/api/locations'],
  });

  // Distance calculation mutation
  const distanceMutation = useMutation({
    mutationFn: async ({ location1Id, location2Id }: { location1Id: string; location2Id: string }) => {
      const response = await apiRequest('POST', '/api/locations/distance', { location1Id, location2Id });
      return response.json();
    },
    onSuccess: (data) => {
      toast({
        title: "Distance Calculated",
        description: `Euclidean distance: ${data.distance}`,
      });
    },
    onError: () => {
      toast({
        title: "Error",
        description: "Failed to calculate distance",
        variant: "destructive",
      });
    }
  });

  // Create location mutation
  const createLocationMutation = useMutation({
    mutationFn: async (location: { x: number; y: number }) => {
      const response = await apiRequest('POST', '/api/locations', location);
      return response.json();
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['/api/locations'] });
      setNewLocation({ x: 0, y: 0 });
      toast({
        title: "Success",
        description: "Location created successfully",
      });
    },
    onError: () => {
      toast({
        title: "Error", 
        description: "Failed to create location",
        variant: "destructive",
      });
    }
  });

  // Delete location mutation
  const deleteLocationMutation = useMutation({
    mutationFn: async (id: string) => {
      await apiRequest('DELETE', `/api/locations/${id}`);
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['/api/locations'] });
      toast({
        title: "Success",
        description: "Location deleted successfully",
      });
    },
    onError: () => {
      toast({
        title: "Error",
        description: "Failed to delete location", 
        variant: "destructive",
      });
    }
  });

  // Clear all locations mutation
  const clearAllMutation = useMutation({
    mutationFn: async () => {
      await apiRequest('DELETE', '/api/locations');
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['/api/locations'] });
      toast({
        title: "Success",
        description: "All locations cleared successfully",
      });
    }
  });

  // Compilation mutation
  const compileMutation = useMutation({
    mutationFn: async (code: string) => {
      const response = await apiRequest('POST', '/api/compile', { 
        sourceCode: code, 
        compileOptions: ['-Wall', '-Wextra', '-std=c++17'] 
      });
      return response.json();
    },
    onSuccess: (data) => {
      setLastCompilationId(data.id);
      setTerminalOutput(data.compileOutput);
      if (data.success) {
        toast({
          title: "Compilation Successful",
          description: "Code compiled without errors",
        });
      } else {
        toast({
          title: "Compilation Failed", 
          description: "Check terminal output for errors",
          variant: "destructive",
        });
      }
    },
    onError: () => {
      toast({
        title: "Error",
        description: "Compilation failed",
        variant: "destructive",
      });
    }
  });

  // Run mutation
  const runMutation = useMutation({
    mutationFn: async ({ compilationId, stdin }: { compilationId: string; stdin: string }) => {
      const response = await apiRequest('POST', `/api/run/${compilationId}`, { stdin });
      return response.json();
    },
    onSuccess: (data) => {
      setTerminalOutput(prev => prev + '\n\n' + data.output);
      toast({
        title: "Execution Complete",
        description: `Program exited with code ${data.exitCode}`,
      });
    },
    onError: () => {
      toast({
        title: "Error", 
        description: "Program execution failed",
        variant: "destructive",
      });
    }
  });

  const handleCreateLocation = () => {
    createLocationMutation.mutate(newLocation);
  };

  const handleCreateDefault = () => {
    createLocationMutation.mutate({ x: 0, y: 0 });
  };

  const handleCalculateDistance = () => {
    if (selectedLocation1 && selectedLocation2) {
      distanceMutation.mutate({ 
        location1Id: selectedLocation1, 
        location2Id: selectedLocation2 
      });
    }
  };

  const handleCompile = () => {
    setIsCompiling(true);
    compileMutation.mutate(sourceCode);
    setIsCompiling(false);
  };

  const handleRun = () => {
    if (lastCompilationId) {
      setIsRunning(true);
      runMutation.mutate({ compilationId: lastCompilationId, stdin: stdinInput });
      setIsRunning(false);
    }
  };

  const handleFileProcessed = (newLocations: Location[]) => {
    queryClient.invalidateQueries({ queryKey: ['/api/locations'] });
  };

  // Statistics
  const statistics = useMemo(() => {
    if (locations.length === 0) return { 
      totalPoints: 0, 
      xRange: "N/A", 
      yRange: "N/A", 
      centroid: "N/A" 
    };
    
    const xCoords = locations.map(loc => loc.x);
    const yCoords = locations.map(loc => loc.y);
    const minX = Math.min(...xCoords);
    const maxX = Math.max(...xCoords);
    const minY = Math.min(...yCoords);
    const maxY = Math.max(...yCoords);
    const centroidX = xCoords.reduce((a, b) => a + b, 0) / xCoords.length;
    const centroidY = yCoords.reduce((a, b) => a + b, 0) / yCoords.length;

    return {
      totalPoints: locations.length,
      xRange: `${minX} to ${maxX}`,
      yRange: `${minY} to ${maxY}`,
      centroid: `(${centroidX.toFixed(2)}, ${centroidY.toFixed(2)})`
    };
  }, [locations]);

  return (
    <div className="flex h-screen bg-background">
      {/* Sidebar */}
      <div className="w-64 bg-card border-r border-border flex flex-col">
        <div className="p-6 border-b border-border">
          <h1 className="text-xl font-bold text-primary flex items-center gap-2">
            <Box className="h-6 w-6" />
            C++ Location IDE
          </h1>
          <p className="text-sm text-muted-foreground mt-1">Interactive Development Environment</p>
        </div>
        
        <nav className="flex-1 p-4">
          <div className="space-y-2">
            <Button
              variant={activeTab === "create" ? "default" : "ghost"}
              className="w-full justify-start"
              onClick={() => setActiveTab("create")}
              data-testid="tab-create"
            >
              <Plus className="mr-3 h-4 w-4" />
              Create Location
            </Button>
            <Button
              variant={activeTab === "import" ? "default" : "ghost"}
              className="w-full justify-start"
              onClick={() => setActiveTab("import")}
              data-testid="tab-import"
            >
              <Upload className="mr-3 h-4 w-4" />
              Import Data
            </Button>
            <Button
              variant={activeTab === "visualize" ? "default" : "ghost"}
              className="w-full justify-start"
              onClick={() => setActiveTab("visualize")}
              data-testid="tab-visualize"
            >
              <ChartScatter className="mr-3 h-4 w-4" />
              Visualize
            </Button>
            <Button
              variant={activeTab === "compile" ? "default" : "ghost"}
              className="w-full justify-start"
              onClick={() => setActiveTab("compile")}
              data-testid="tab-compile"
            >
              <Settings className="mr-3 h-4 w-4" />
              Compile & Run
            </Button>
          </div>
          
          <div className="mt-8 pt-4 border-t border-border">
            <h3 className="text-xs font-semibold text-muted-foreground uppercase tracking-wider">Statistics</h3>
            <div className="mt-2 space-y-1">
              <div className="text-sm">
                <span className="text-muted-foreground">Total Objects:</span>
                <span className="text-foreground font-mono ml-2" data-testid="text-total-objects">
                  {locations.length}
                </span>
              </div>
              <div className="text-sm">
                <span className="text-muted-foreground">Active Memory:</span>
                <span className="text-success font-mono ml-2">
                  {locations.length * 48} bytes
                </span>
              </div>
            </div>
          </div>
        </nav>
      </div>

      {/* Main Content */}
      <div className="flex-1 flex flex-col overflow-hidden">
        {/* Header */}
        <header className="bg-card border-b border-border px-6 py-4">
          <div className="flex items-center justify-between">
            <div>
              <h2 className="text-lg font-semibold text-foreground">Location Object Manager</h2>
              <p className="text-sm text-muted-foreground">Create, manage, and visualize coordinate locations</p>
            </div>
            <div className="flex items-center space-x-3">
              <div className="flex items-center space-x-2 text-sm text-muted-foreground">
                <div className="w-2 h-2 rounded-full bg-success"></div>
                <span>Compiler Ready</span>
              </div>
              <Button data-testid="button-save-project">
                <Save className="mr-2 h-4 w-4" />
                Save Project
              </Button>
            </div>
          </div>
        </header>

        {/* Main Content Area */}
        <main className="flex-1 overflow-auto p-6">
          {activeTab === "create" && (
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 h-full">
              {/* Location Creation Form */}
              <Card>
                <CardHeader>
                  <CardTitle className="flex items-center gap-2">
                    <MapPin className="h-5 w-5 text-primary" />
                    Create Location Objects
                  </CardTitle>
                </CardHeader>
                <CardContent className="space-y-6">
                  {/* Single Location Form */}
                  <div className="space-y-4">
                    <div className="grid grid-cols-2 gap-4">
                      <div>
                        <Label htmlFor="x-coord">X Coordinate</Label>
                        <Input
                          id="x-coord"
                          type="number"
                          value={newLocation.x}
                          onChange={(e) => setNewLocation({ ...newLocation, x: parseInt(e.target.value) || 0 })}
                          className="font-mono"
                          data-testid="input-x-coordinate"
                        />
                      </div>
                      <div>
                        <Label htmlFor="y-coord">Y Coordinate</Label>
                        <Input
                          id="y-coord"
                          type="number"
                          value={newLocation.y}
                          onChange={(e) => setNewLocation({ ...newLocation, y: parseInt(e.target.value) || 0 })}
                          className="font-mono"
                          data-testid="input-y-coordinate"
                        />
                      </div>
                    </div>
                    
                    <div className="flex space-x-3">
                      <Button 
                        className="flex-1"
                        onClick={handleCreateLocation}
                        disabled={createLocationMutation.isPending}
                        data-testid="button-create-location"
                      >
                        <Plus className="mr-2 h-4 w-4" />
                        Create Location
                      </Button>
                      <Button 
                        variant="secondary"
                        onClick={handleCreateDefault}
                        disabled={createLocationMutation.isPending}
                        data-testid="button-create-default"
                      >
                        <Home className="mr-2 h-4 w-4" />
                        Default (0,0)
                      </Button>
                    </div>
                  </div>

                  {/* Distance Calculator */}
                  <div className="pt-6 border-t border-border">
                    <h4 className="text-md font-semibold text-foreground mb-4 flex items-center gap-2">
                      <Calculator className="h-4 w-4 text-accent" />
                      Distance Calculator
                    </h4>
                    <div className="space-y-3">
                      <div className="grid grid-cols-2 gap-4">
                        <Select value={selectedLocation1} onValueChange={setSelectedLocation1}>
                          <SelectTrigger data-testid="select-location-1">
                            <SelectValue placeholder="Select Location 1" />
                          </SelectTrigger>
                          <SelectContent>
                            {locations.map((loc) => (
                              <SelectItem key={loc.id} value={loc.id}>
                                ({loc.x}, {loc.y})
                              </SelectItem>
                            ))}
                          </SelectContent>
                        </Select>
                        <Select value={selectedLocation2} onValueChange={setSelectedLocation2}>
                          <SelectTrigger data-testid="select-location-2">
                            <SelectValue placeholder="Select Location 2" />
                          </SelectTrigger>
                          <SelectContent>
                            {locations.map((loc) => (
                              <SelectItem key={loc.id} value={loc.id}>
                                ({loc.x}, {loc.y})
                              </SelectItem>
                            ))}
                          </SelectContent>
                        </Select>
                      </div>
                      <Button 
                        className="w-full"
                        variant="secondary"
                        onClick={handleCalculateDistance}
                        disabled={!selectedLocation1 || !selectedLocation2 || distanceMutation.isPending}
                        data-testid="button-calculate-distance"
                      >
                        <Calculator className="mr-2 h-4 w-4" />
                        Calculate Euclidean Distance
                      </Button>
                    </div>
                  </div>
                </CardContent>
              </Card>

              {/* Location Objects Table */}
              <Card>
                <CardHeader>
                  <div className="flex items-center justify-between">
                    <CardTitle className="flex items-center gap-2">
                      <MapPin className="h-5 w-5 text-primary" />
                      Location Objects
                    </CardTitle>
                    <div className="flex items-center space-x-2">
                      <Button 
                        size="sm"
                        variant="secondary"
                        onClick={() => clearAllMutation.mutate()}
                        disabled={clearAllMutation.isPending}
                        data-testid="button-clear-all"
                      >
                        <Trash2 className="h-4 w-4" />
                      </Button>
                      <Button 
                        size="sm"
                        variant="secondary"
                        data-testid="button-export-data"
                      >
                        <Download className="h-4 w-4" />
                      </Button>
                    </div>
                  </div>
                </CardHeader>
                <CardContent>
                  <div className="overflow-auto h-96">
                    {locationsLoading ? (
                      <div className="flex items-center justify-center h-32">
                        <div className="text-muted-foreground">Loading locations...</div>
                      </div>
                    ) : locations.length === 0 ? (
                      <div className="flex items-center justify-center h-32">
                        <div className="text-muted-foreground">No locations created yet</div>
                      </div>
                    ) : (
                      <Table>
                        <TableHeader>
                          <TableRow>
                            <TableHead>#</TableHead>
                            <TableHead>X</TableHead>
                            <TableHead>Y</TableHead>
                            <TableHead>String</TableHead>
                            <TableHead>Actions</TableHead>
                          </TableRow>
                        </TableHeader>
                        <TableBody>
                          {locations.map((location, index) => (
                            <TableRow key={location.id} data-testid={`row-location-${location.id}`}>
                              <TableCell className="font-mono text-muted-foreground">
                                {index + 1}
                              </TableCell>
                              <TableCell className="font-mono text-primary">
                                {location.x}
                              </TableCell>
                              <TableCell className="font-mono text-primary">
                                {location.y}
                              </TableCell>
                              <TableCell className="font-mono text-foreground">
                                ({location.x},{location.y})
                              </TableCell>
                              <TableCell>
                                <Button
                                  size="sm"
                                  variant="ghost"
                                  onClick={() => deleteLocationMutation.mutate(location.id)}
                                  disabled={deleteLocationMutation.isPending}
                                  className="text-destructive hover:text-destructive/80"
                                  data-testid={`button-delete-${location.id}`}
                                >
                                  <Trash2 className="h-4 w-4" />
                                </Button>
                              </TableCell>
                            </TableRow>
                          ))}
                        </TableBody>
                      </Table>
                    )}
                  </div>
                </CardContent>
              </Card>
            </div>
          )}

          {activeTab === "import" && (
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 h-full">
              <div>
                <Card>
                  <CardHeader>
                    <CardTitle className="flex items-center gap-2">
                      <Upload className="h-5 w-5 text-primary" />
                      Import Location Data
                    </CardTitle>
                  </CardHeader>
                  <CardContent>
                    <FileUpload onFileProcessed={handleFileProcessed} />
                  </CardContent>
                </Card>
              </div>
              <div>
                <Card>
                  <CardHeader>
                    <CardTitle>Current Data</CardTitle>
                  </CardHeader>
                  <CardContent>
                    <div className="text-sm space-y-2">
                      <div>
                        <span className="text-muted-foreground">Total Locations:</span>{' '}
                        <span className="text-foreground font-mono">{locations.length}</span>
                      </div>
                      {locations.length > 0 && (
                        <div className="mt-4">
                          <div className="text-muted-foreground mb-2">Recent locations:</div>
                          <div className="space-y-1">
                            {locations.slice(-5).map((loc, index) => (
                              <div key={loc.id} className="font-mono text-sm">
                                ({loc.x}, {loc.y})
                              </div>
                            ))}
                          </div>
                        </div>
                      )}
                    </div>
                  </CardContent>
                </Card>
              </div>
            </div>
          )}

          {activeTab === "visualize" && (
            <div className="grid grid-cols-1 xl:grid-cols-3 gap-6 h-full">
              {/* 2D Plot Visualization */}
              <div className="xl:col-span-2">
                <Card>
                  <CardHeader>
                    <div className="flex items-center justify-between">
                      <CardTitle className="flex items-center gap-2">
                        <ChartScatter className="h-5 w-5 text-primary" />
                        2D Coordinate Plot
                      </CardTitle>
                    </div>
                  </CardHeader>
                  <CardContent>
                    <LocationPlot locations={locations} className="h-[500px]" />
                    <div className="mt-4 flex items-center justify-between">
                      <div className="text-sm text-muted-foreground">
                        Showing <span className="text-foreground font-medium">{locations.length}</span> locations
                      </div>
                    </div>
                  </CardContent>
                </Card>
              </div>

              {/* Plot Controls & Analysis */}
              <div className="space-y-6">
                {/* Plot Legend */}
                <Card>
                  <CardHeader>
                    <CardTitle className="text-md">Legend</CardTitle>
                  </CardHeader>
                  <CardContent>
                    <div className="space-y-2">
                      {locations.slice(0, 5).map((location, index) => {
                        const colors = ['bg-primary', 'bg-accent', 'bg-success', 'bg-warning', 'bg-chart-2'];
                        return (
                          <div key={location.id} className="flex items-center">
                            <div className={`w-3 h-3 rounded-full ${colors[index]} mr-3`}></div>
                            <span className="text-sm text-foreground">({location.x}, {location.y})</span>
                          </div>
                        );
                      })}
                    </div>
                  </CardContent>
                </Card>

                {/* Statistical Analysis */}
                <Card>
                  <CardHeader>
                    <CardTitle className="text-md">Analysis</CardTitle>
                  </CardHeader>
                  <CardContent>
                    <div className="space-y-3 text-sm">
                      <div className="flex justify-between">
                        <span className="text-muted-foreground">Total Points:</span>
                        <span className="text-foreground font-mono">{statistics.totalPoints}</span>
                      </div>
                      <div className="flex justify-between">
                        <span className="text-muted-foreground">X Range:</span>
                        <span className="text-foreground font-mono">{statistics.xRange}</span>
                      </div>
                      <div className="flex justify-between">
                        <span className="text-muted-foreground">Y Range:</span>
                        <span className="text-foreground font-mono">{statistics.yRange}</span>
                      </div>
                      <div className="flex justify-between">
                        <span className="text-muted-foreground">Centroid:</span>
                        <span className="text-foreground font-mono">{statistics.centroid}</span>
                      </div>
                    </div>
                  </CardContent>
                </Card>
              </div>
            </div>
          )}

          {activeTab === "compile" && (
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 h-full">
              {/* C++ Code Editor */}
              <Card>
                <CardHeader>
                  <div className="flex items-center justify-between">
                    <CardTitle className="flex items-center gap-2">
                      <Code className="h-5 w-5 text-primary" />
                      C++ Source Code
                    </CardTitle>
                    <div className="flex items-center space-x-2">
                      <Button 
                        size="sm"
                        onClick={handleCompile}
                        disabled={compileMutation.isPending || isCompiling}
                        data-testid="button-compile"
                      >
                        <Settings className="mr-1 h-4 w-4" />
                        {isCompiling ? 'Compiling...' : 'Compile'}
                      </Button>
                      <Button 
                        size="sm"
                        variant="secondary"
                        onClick={handleRun}
                        disabled={!lastCompilationId || runMutation.isPending || isRunning}
                        data-testid="button-run"
                      >
                        <Play className="mr-1 h-4 w-4" />
                        {isRunning ? 'Running...' : 'Run'}
                      </Button>
                    </div>
                  </div>
                </CardHeader>
                <CardContent className="space-y-4">
                  <Textarea
                    value={sourceCode}
                    onChange={(e) => setSourceCode(e.target.value)}
                    className="font-mono text-sm h-80 bg-background"
                    placeholder="Enter your C++ code here..."
                    data-testid="textarea-source-code"
                  />
                  <div>
                    <Label className="text-sm text-muted-foreground mb-1 block">
                      Program Input (stdin) — one value per line or space-separated
                    </Label>
                    <Textarea
                      value={stdinInput}
                      onChange={(e) => setStdinInput(e.target.value)}
                      className="font-mono text-sm h-20 bg-background"
                      placeholder="e.g. 2 3&#10;0 0"
                      data-testid="textarea-stdin"
                    />
                  </div>
                </CardContent>
              </Card>

              {/* Terminal Output */}
              <TerminalOutput 
                output={terminalOutput}
                isRunning={isRunning}
                onClear={() => setTerminalOutput("")}
              />
            </div>
          )}
        </main>
      </div>
    </div>
  );
}
