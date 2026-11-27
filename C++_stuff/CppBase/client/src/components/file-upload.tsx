import { useState, useCallback } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Upload, FileText, CheckCircle, AlertCircle } from "lucide-react";
import { useToast } from "@/hooks/use-toast";

interface FileUploadProps {
  onFileProcessed: (locations: any[]) => void;
}

export function FileUpload({ onFileProcessed }: FileUploadProps) {
  const [isDragging, setIsDragging] = useState(false);
  const [isProcessing, setIsProcessing] = useState(false);
  const [previewData, setPreviewData] = useState<{
    filename: string;
    lines: { x: number; y: number; valid: boolean; error?: string }[];
  } | null>(null);
  const { toast } = useToast();

  const validateFileContent = useCallback((content: string, filename: string) => {
    const lines = content.trim().split('\n');
    const parsedLines = lines.map((line, index) => {
      const trimmed = line.trim();
      if (!trimmed) return null;
      
      const parts = trimmed.split(/\s+/);
      if (parts.length !== 2) {
        return { x: 0, y: 0, valid: false, error: `Invalid format at line ${index + 1}` };
      }
      
      const x = parseInt(parts[0]);
      const y = parseInt(parts[1]);
      
      if (isNaN(x) || isNaN(y)) {
        return { x: 0, y: 0, valid: false, error: `Invalid coordinates at line ${index + 1}` };
      }
      
      return { x, y, valid: true };
    }).filter(Boolean) as { x: number; y: number; valid: boolean; error?: string }[];

    setPreviewData({ filename, lines: parsedLines });
    return parsedLines;
  }, []);

  const handleFile = useCallback(async (file: File) => {
    setIsProcessing(true);
    try {
      const content = await file.text();
      const validatedLines = validateFileContent(content, file.name);
      
      const formData = new FormData();
      formData.append('file', file);
      
      const response = await fetch('/api/files/upload', {
        method: 'POST',
        body: formData,
      });
      
      if (!response.ok) {
        const error = await response.json();
        throw new Error(error.message || 'Upload failed');
      }
      
      const result = await response.json();
      onFileProcessed(result.locations);
      
      toast({
        title: "File uploaded successfully",
        description: result.message,
      });
    } catch (error) {
      toast({
        title: "Upload failed",
        description: error instanceof Error ? error.message : 'Unknown error occurred',
        variant: "destructive",
      });
    } finally {
      setIsProcessing(false);
    }
  }, [validateFileContent, onFileProcessed, toast]);

  const handleDrop = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);
    
    const files = Array.from(e.dataTransfer.files);
    const txtFile = files.find(f => f.name.endsWith('.txt') || f.name.endsWith('.dat'));
    
    if (txtFile) {
      handleFile(txtFile);
    } else {
      toast({
        title: "Invalid file type",
        description: "Please upload a .txt or .dat file",
        variant: "destructive",
      });
    }
  }, [handleFile, toast]);

  const handleFileSelect = useCallback((e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      handleFile(file);
    }
  }, [handleFile]);

  return (
    <div className="space-y-6">
      {/* File Drop Zone */}
      <Card 
        className={`border-2 border-dashed transition-colors ${
          isDragging ? 'border-primary/50 bg-primary/5' : 'border-border'
        } hover:border-primary/50`}
        onDragOver={(e) => { e.preventDefault(); setIsDragging(true); }}
        onDragLeave={() => setIsDragging(false)}
        onDrop={handleDrop}
        data-testid="file-drop-zone"
      >
        <CardContent className="p-8 text-center">
          <div className="mb-4">
            <Upload className="h-12 w-12 text-muted-foreground mx-auto" />
          </div>
          <p className="text-foreground font-medium mb-2">Drop your LocationData.txt file here</p>
          <p className="text-sm text-muted-foreground mb-4">or click to browse</p>
          <input 
            type="file" 
            className="hidden" 
            accept=".txt,.dat" 
            onChange={handleFileSelect}
            id="file-input"
            data-testid="file-input"
          />
          <Button 
            onClick={() => document.getElementById('file-input')?.click()}
            disabled={isProcessing}
            data-testid="button-choose-file"
          >
            {isProcessing ? 'Processing...' : 'Choose File'}
          </Button>
        </CardContent>
      </Card>

      {/* File Format Guide */}
      <Card>
        <CardContent className="p-6">
          <h4 className="text-md font-semibold text-foreground mb-3">Expected File Format</h4>
          <div className="bg-muted rounded-md p-4">
            <pre className="text-sm font-mono text-muted-foreground">
{`2 3
0 0
-1 3
-9 -3`}
            </pre>
          </div>
          <p className="text-xs text-muted-foreground mt-2">
            Each line contains X and Y coordinates separated by a space
          </p>
        </CardContent>
      </Card>

      {/* Import Preview */}
      {previewData && (
        <Card>
          <CardContent className="p-6">
            <h4 className="text-md font-semibold text-foreground mb-4">
              <FileText className="inline h-4 w-4 mr-2 text-primary" />
              Import Preview
            </h4>
            
            <div className="space-y-4">
              {/* File Info */}
              <div className="bg-muted rounded-md p-4">
                <div className="text-sm space-y-1">
                  <div>
                    <span className="text-muted-foreground">File:</span>{' '}
                    <span className="text-foreground font-mono">{previewData.filename}</span>
                  </div>
                  <div>
                    <span className="text-muted-foreground">Lines:</span>{' '}
                    <span className="text-success">{previewData.lines.length} locations detected</span>
                  </div>
                </div>
              </div>

              {/* Preview Table */}
              <div className="overflow-auto max-h-64">
                <table className="w-full text-sm">
                  <thead className="bg-muted rounded-t-md">
                    <tr>
                      <th className="px-3 py-2 text-left text-muted-foreground font-medium">Line</th>
                      <th className="px-3 py-2 text-left text-muted-foreground font-medium">X</th>
                      <th className="px-3 py-2 text-left text-muted-foreground font-medium">Y</th>
                      <th className="px-3 py-2 text-left text-muted-foreground font-medium">Status</th>
                    </tr>
                  </thead>
                  <tbody>
                    {previewData.lines.map((line, index) => (
                      <tr key={index} className="border-t border-border">
                        <td className="px-3 py-2 font-mono text-muted-foreground">{index + 1}</td>
                        <td className="px-3 py-2 font-mono text-primary">{line.x}</td>
                        <td className="px-3 py-2 font-mono text-primary">{line.y}</td>
                        <td className="px-3 py-2">
                          {line.valid ? (
                            <span className="text-xs px-2 py-1 bg-success/20 text-success rounded flex items-center gap-1">
                              <CheckCircle className="h-3 w-3" />
                              Valid
                            </span>
                          ) : (
                            <span className="text-xs px-2 py-1 bg-destructive/20 text-destructive rounded flex items-center gap-1">
                              <AlertCircle className="h-3 w-3" />
                              Error
                            </span>
                          )}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>

              {/* Import Summary */}
              {previewData.lines.every(line => line.valid) ? (
                <div className="bg-success/10 border border-success/20 rounded-md p-4">
                  <div className="flex items-center">
                    <CheckCircle className="text-success mr-2 h-4 w-4" />
                    <span className="text-sm font-medium text-success">Ready to Import</span>
                  </div>
                  <p className="text-xs text-success/80 mt-1">
                    {previewData.lines.length} valid locations will be added to your dataset
                  </p>
                </div>
              ) : (
                <div className="bg-destructive/10 border border-destructive/20 rounded-md p-4">
                  <div className="flex items-center">
                    <AlertCircle className="text-destructive mr-2 h-4 w-4" />
                    <span className="text-sm font-medium text-destructive">Import Issues Found</span>
                  </div>
                  <p className="text-xs text-destructive/80 mt-1">
                    Please fix the errors before importing
                  </p>
                </div>
              )}
            </div>
          </CardContent>
        </Card>
      )}
    </div>
  );
}
