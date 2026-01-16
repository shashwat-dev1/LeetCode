class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7
        hBoundaries = sorted([1] + hFences + [m])
        vBoundaries = sorted([1] + vFences + [n])
        hGaps = set()
        for i in range(len(hBoundaries)):
            for j in range(i + 1, len(hBoundaries)):
                hGaps.add(hBoundaries[j] - hBoundaries[i])
        vGaps = set()
        for i in range(len(vBoundaries)):
            for j in range(i + 1, len(vBoundaries)):
                vGaps.add(vBoundaries[j] - vBoundaries[i])
        commonGaps = hGaps & vGaps
        if not commonGaps:
            return -1
        maxSide = max(commonGaps)
        return (maxSide * maxSide) % MOD