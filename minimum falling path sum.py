class Solution:
    def minFallingPathSum(self, matrix) -> int:
        m, n = len(matrix), len(matrix[0])
        t = [[10000 for _ in range(n + 2)] for _ in range(m + 1)]

        for i in range(n + 2):
            t[m][i] = 0

        for i in range(m - 1, -1, -1):
            for j in range(1, n + 1):
                # print(i, j)
                t[i][j] = min(t[i + 1][j - 1], t[i + 1][j], t[i + 1][j + 1]) + matrix[i][j - 1]

        return min(t[0])
