class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        maxArea = 0
        for i in range(n):
            for j in range(i + 1, n):
                overlapLeft = max(bottomLeft[i][0], bottomLeft[j][0])
                overlapRight = min(topRight[i][0], topRight[j][0])
                overlapBottom = max(bottomLeft[i][1], bottomLeft[j][1])
                overlapTop = min(topRight[i][1], topRight[j][1])
                if overlapLeft < overlapRight and overlapBottom < overlapTop:
                    width = overlapRight - overlapLeft
                    height = overlapTop - overlapBottom
                    side = min(width, height)
                    area = side * side
                    
                    maxArea = max(maxArea, area)
        
        return maxArea