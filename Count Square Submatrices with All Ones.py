class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        t = [[0 for _ in range(n)] for _ in range(m)]
        ans = 0

        for i in range(n):
            if matrix[m - 1][i] == 1:
                t[m - 1][i] = 1
                ans += t[m - 1][i]

        for i in range(m - 1):
            if matrix[i][n - 1] == 1:
                t[i][n - 1] = 1
                ans += t[i][n - 1]

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if matrix[i][j] != 0:
                    t[i][j] = min(t[i][j + 1], t[i + 1][j + 1], t[i + 1][j]) + 1
                    ans += t[i][j]

        return ans
