class Solution:
    def sumRegion(self, matrix, row1, col1, row2, col2):
        ans = 0
        for i in range(row1, row2 + 1):
            x1 = matrix[i][col2]
            x2 = 0 if col1 == 0 else matrix[i][col1 - 1]
            ans += x1 - x2
        return ans

    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        t = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            sums = 0
            for j in range(n):
                sums += mat[i][j]
                t[i][j] = sums

        for i in range(m):
            for j in range(n):
                r1, r2 = max(0, i - k), min(m - 1, i + k)
                c1, c2 = max(0, j - k), min(n - 1, j + k)
                mat[i][j] = self.sumRegion(t, r1, c1, r2, c2)

        return mat