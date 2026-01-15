class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0
        max_left = height[0]      
        max_right = height[n - 1] 
        trapped_water = 0
        left = 1
        right = n - 2
        while left <= right:
            if max_left < max_right:
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    trapped_water += max_left - height[left]
                left += 1
            else:
                if height[right] > max_right:
                    max_right = height[right]
                else:
                    trapped_water += max_right - height[right]
                right -= 1
        return trapped_water