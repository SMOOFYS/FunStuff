import { useState, useEffect, useRef } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Terminal, Play, Settings, Trash2 } from "lucide-react";

interface TerminalOutputProps {
  output: string;
  isRunning?: boolean;
  onClear?: () => void;
}

export function TerminalOutput({ output, isRunning = false, onClear }: TerminalOutputProps) {
  const [displayedOutput, setDisplayedOutput] = useState("");
  const outputRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (isRunning && output) {
      // Simulate typing effect
      let currentIndex = 0;
      const interval = setInterval(() => {
        if (currentIndex < output.length) {
          setDisplayedOutput(output.slice(0, currentIndex + 1));
          currentIndex++;
        } else {
          clearInterval(interval);
        }
      }, 10);
      
      return () => clearInterval(interval);
    } else {
      setDisplayedOutput(output);
    }
  }, [output, isRunning]);

  useEffect(() => {
    // Auto-scroll to bottom
    if (outputRef.current) {
      outputRef.current.scrollTop = outputRef.current.scrollHeight;
    }
  }, [displayedOutput]);

  return (
    <Card>
      <CardHeader className="pb-3">
        <div className="flex items-center justify-between">
          <CardTitle className="text-lg font-semibold text-foreground flex items-center gap-2">
            <Terminal className="h-5 w-5 text-primary" />
            Terminal Output
          </CardTitle>
          <div className="flex items-center space-x-2">
            <div className="flex items-center space-x-1 text-xs">
              <div className={`w-2 h-2 rounded-full ${isRunning ? 'bg-warning animate-pulse' : 'bg-success'}`}></div>
              <span className="text-muted-foreground">{isRunning ? 'Running' : 'Ready'}</span>
            </div>
            {onClear && (
              <Button 
                size="sm" 
                variant="secondary"
                onClick={onClear}
                data-testid="button-clear-terminal"
              >
                <Trash2 className="h-4 w-4" />
              </Button>
            )}
          </div>
        </div>
      </CardHeader>
      <CardContent>
        <div 
          ref={outputRef}
          className="terminal-output"
          data-testid="terminal-output"
        >
          {displayedOutput || "Ready to compile and run C++ code..."}
          {isRunning && <span className="animate-pulse">_</span>}
        </div>

        {/* Build Information */}
        <div className="mt-4 space-y-3">
          <Card className="bg-muted/50">
            <CardContent className="p-3">
              <h4 className="text-sm font-semibold text-foreground mb-2 flex items-center gap-2">
                <Settings className="h-4 w-4" />
                Build Information
              </h4>
              <div className="text-xs space-y-1">
                <div>
                  <span className="text-muted-foreground">Compiler:</span>{' '}
                  <span className="text-foreground font-mono">g++ 11.3.0</span>
                </div>
                <div>
                  <span className="text-muted-foreground">Standard:</span>{' '}
                  <span className="text-foreground font-mono">C++17</span>
                </div>
                <div>
                  <span className="text-muted-foreground">Build Time:</span>{' '}
                  <span className="text-success font-mono">1.23s</span>
                </div>
                <div>
                  <span className="text-muted-foreground">Binary Size:</span>{' '}
                  <span className="text-foreground font-mono">24.5 KB</span>
                </div>
              </div>
            </CardContent>
          </Card>

          <Card className="bg-muted/50">
            <CardContent className="p-3">
              <h4 className="text-sm font-semibold text-foreground mb-2 flex items-center gap-2">
                <Play className="h-4 w-4" />
                Runtime Statistics
              </h4>
              <div className="text-xs space-y-1">
                <div>
                  <span className="text-muted-foreground">Objects Created:</span>{' '}
                  <span className="text-primary font-mono">10</span>
                </div>
                <div>
                  <span className="text-muted-foreground">Memory Used:</span>{' '}
                  <span className="text-foreground font-mono">480 bytes</span>
                </div>
                <div>
                  <span className="text-muted-foreground">Execution Time:</span>{' '}
                  <span className="text-success font-mono">0.002s</span>
                </div>
                <div>
                  <span className="text-muted-foreground">Exit Code:</span>{' '}
                  <span className="text-success font-mono">0</span>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>
      </CardContent>
    </Card>
  );
}
