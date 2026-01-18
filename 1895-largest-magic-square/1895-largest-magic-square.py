class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rowsum = [[0] * (n + 1) for _ in range(m + 1)]
        colsum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                rowsum[i][j] = rowsum[i][j - 1] + grid[i - 1][j - 1]
                colsum[i][j] = colsum[i - 1][j] + grid[i - 1][j - 1]
        for k in range(min(m, n), 1, -1):
            for x1 in range(m - k + 1):
                for y1 in range(n - k + 1):
                    x2, y2 = x1 + k, y1 + k
                    target = rowsum[x1 + 1][y2] - rowsum[x1 + 1][y1]
                    valid = all(
                        rowsum[i][y2] - rowsum[i][y1] == target
                        for i in range(x1 + 1, x2 + 1)
                    )
                    if not valid:
                        continue
                    valid = all(
                        colsum[x2][j] - colsum[x1][j] == target
                        for j in range(y1 + 1, y2 + 1)
                    )
                    if not valid:
                        continue
                    diag1 = sum(grid[x1 + i][y1 + i] for i in range(k))
                    if diag1 != target:
                        continue
                    diag2 = sum(grid[x1 + i][y2 - 1 - i] for i in range(k))
                    if diag2 == target:
                        return k
        return 1