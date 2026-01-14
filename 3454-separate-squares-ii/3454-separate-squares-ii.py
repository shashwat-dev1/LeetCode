from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        if not squares:
            return 0.0
        
        # Create sweep events
        events = []
        for x, y, l in squares:
            events.append((y, 1, x, x + l))      # Start of square
            events.append((y + l, -1, x, x + l)) # End of square
        
        events.sort()
        
        # First pass: compute strips with their areas
        active_intervals = []
        strips = []  # (y_start, height, union_width)
        total_area = 0.0
        prev_y = events[0][0]
        
        for y, event_type, x_start, x_end in events:
            # Process strip between prev_y and current y
            if y > prev_y:
                width = self.get_union_width(active_intervals)
                height = y - prev_y
                
                if width > 0:
                    strips.append((prev_y, height, width))
                    total_area += height * width
            
            # Update active intervals
            if event_type == 1:  # Start
                active_intervals.append((x_start, x_end))
            else:  # End
                active_intervals.remove((x_start, x_end))
            
            prev_y = y
        
        # Second pass: find exact cut line
        target_area = total_area / 2.0
        accumulated_area = 0.0
        
        for y_start, height, width in strips:
            strip_area = height * width
            
            if accumulated_area + strip_area >= target_area:
                # The cut line is within this strip
                area_needed = target_area - accumulated_area
                return y_start + (area_needed / width)
            
            accumulated_area += strip_area
        
        return 0.0
    
    def get_union_width(self, intervals):
        if not intervals:
            return 0
        
        sorted_intervals = sorted(intervals)
        union_length = 0
        current_end = float('-inf')
        
        for start, end in sorted_intervals:
            if start >= current_end:
                # No overlap, add full length
                union_length += (end - start)
                current_end = end
            elif end > current_end:
                # Partial overlap, extend current end
                union_length += (end - current_end)
                current_end = end
        
        return union_length