import { Location } from "@shared/schema";
import { useMemo } from "react";

interface LocationPlotProps {
  locations: Location[];
  className?: string;
}

export function LocationPlot({ locations, className = "" }: LocationPlotProps) {
  const plotData = useMemo(() => {
    if (locations.length === 0) return { points: [], bounds: { minX: -10, maxX: 10, minY: -10, maxY: 10 } };

    const xCoords = locations.map(loc => loc.x);
    const yCoords = locations.map(loc => loc.y);
    
    const minX = Math.min(...xCoords, -5);
    const maxX = Math.max(...xCoords, 5);
    const minY = Math.min(...yCoords, -5);
    const maxY = Math.max(...yCoords, 5);
    
    // Add padding
    const xRange = maxX - minX;
    const yRange = maxY - minY;
    const padding = Math.max(xRange, yRange) * 0.1;
    
    const bounds = {
      minX: minX - padding,
      maxX: maxX + padding,
      minY: minY - padding,
      maxY: maxY + padding
    };

    const points = locations.map((loc, index) => {
      const xPercent = ((loc.x - bounds.minX) / (bounds.maxX - bounds.minX)) * 100;
      const yPercent = 100 - ((loc.y - bounds.minY) / (bounds.maxY - bounds.minY)) * 100; // Flip Y axis
      
      const colors = ['bg-primary', 'bg-accent', 'bg-success', 'bg-warning', 'bg-chart-2'];
      
      return {
        x: xPercent,
        y: yPercent,
        location: loc,
        color: colors[index % colors.length]
      };
    });

    return { points, bounds };
  }, [locations]);

  const { points, bounds } = plotData;

  return (
    <div className={`relative bg-background border border-border rounded-lg p-4 ${className}`}>
      <div className="absolute inset-4 plot-grid">
        {/* Axes */}
        <div className="absolute left-1/2 top-0 w-px h-full bg-primary/30 transform -translate-x-px"></div>
        <div className="absolute top-1/2 left-0 w-full h-px bg-primary/30 transform -translate-y-px"></div>
        
        {/* Axis Labels */}
        <div className="absolute -bottom-6 left-1/2 transform -translate-x-1/2 text-xs text-muted-foreground font-mono">X</div>
        <div className="absolute -left-6 top-1/2 transform -translate-y-1/2 rotate-90 text-xs text-muted-foreground font-mono">Y</div>
        
        {/* Coordinate Points */}
        {points.map((point, index) => (
          <div 
            key={point.location.id}
            className={`coordinate-point ${point.color}`}
            style={{ left: `${point.x}%`, top: `${point.y}%` }}
            title={`(${point.location.x}, ${point.location.y})`}
            data-testid={`coordinate-point-${point.location.id}`}
          />
        ))}
        
        {/* Grid Scale Markers */}
        <div className="absolute bottom-2 left-2 text-xs text-muted-foreground font-mono">
          {Math.round(bounds.minX)}
        </div>
        <div className="absolute bottom-2 right-2 text-xs text-muted-foreground font-mono">
          {Math.round(bounds.maxX)}
        </div>
        <div className="absolute top-2 left-2 text-xs text-muted-foreground font-mono">
          {Math.round(bounds.maxY)}
        </div>
        <div className="absolute bottom-2 left-1/2 transform -translate-x-1/2 text-xs text-muted-foreground font-mono">
          {Math.round((bounds.minX + bounds.maxX) / 2)}
        </div>
      </div>
      
      {locations.length === 0 && (
        <div className="absolute inset-0 flex items-center justify-center">
          <p className="text-muted-foreground text-sm">No locations to display</p>
        </div>
      )}
    </div>
  );
}
