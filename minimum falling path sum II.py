class Solution:
    def minFallingPathSum(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        t = [[100000000 for _ in range(n + 2)] for _ in range(m + 1)]

        for i in range(n + 2):
            t[m][i] = 0

        for i in range(m - 1, -1, -1):
            for j in range(1, n + 1):
                temp = []
                for k in range(n + 2):
                    if k != j:
                        temp.append(t[i + 1][k])
                t[i][j] = min(temp) + grid[i][j - 1]

        return min(t[0])
