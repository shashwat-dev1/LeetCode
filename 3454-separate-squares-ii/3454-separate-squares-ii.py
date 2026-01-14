from typing import List
from collections import defaultdict

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        if not squares:
            return 0.0
        
        # Create events for horizontal sweep
        events = []
        for x, y, l in squares:
            events.append((y, 0, x, x + l))      # Bottom edge (square starts)
            events.append((y + l, 1, x, x + l))  # Top edge (square ends)
        
        events.sort()
        
        # Track cumulative area as we sweep upward
        y_to_area_below = {}  # Maps y-coordinate to total area below that y
        
        active_intervals = []  # Currently active x-intervals
        prev_y = None
        cumulative_area = 0.0
        
        for y, event_type, x1, x2 in events:
            if prev_y is not None and prev_y != y:
                # Calculate width at this height
                width = self.merge_intervals_length(active_intervals)
                height = y - prev_y
                cumulative_area += width * height
            
            y_to_area_below[y] = cumulative_area
            
            if event_type == 0:  # Start
                active_intervals.append((x1, x2))
            else:  # End
                active_intervals.remove((x1, x2))
            
            prev_y = y
        
        # Total area
        total_area = cumulative_area
        target_area = total_area / 2.0
        
        # Find the y-coordinate where area below equals target
        y_coords = sorted(y_to_area_below.keys())
        
        for i in range(len(y_coords)):
            y = y_coords[i]
            area_below = y_to_area_below[y]
            
            if abs(area_below - target_area) < 1e-9:
                return float(y)
            
            if area_below >= target_area:
                if i == 0:
                    return float(y)
                
                # Interpolate between y_coords[i-1] and y_coords[i]
                y_prev = y_coords[i - 1]
                area_prev = y_to_area_below[y_prev]
                
                if abs(area_below - area_prev) < 1e-9:
                    return float(y)
                
                # Linear interpolation
                t = (target_area - area_prev) / (area_below - area_prev)
                result = y_prev + t * (y - y_prev)
                return float(result)
        
        return float(y_coords[-1])
    
    def merge_intervals_length(self, intervals):
        if not intervals:
            return 0
        
        sorted_intervals = sorted(intervals)
        total = 0
        current_start, current_end = sorted_intervals[0]
        
        for start, end in sorted_intervals[1:]:
            if start <= current_end:
                current_end = max(current_end, end)
            else:
                total += current_end - current_start
                current_start, current_end = start, end
        
        total += current_end - current_start
        return total