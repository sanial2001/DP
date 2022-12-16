class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        t = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for r, c, p in prices:
            t[r][c] = p

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for c in range(j):
                    t[i][j] = max(t[i][j], t[i][c] + t[i][j - c])
                for r in range(i):
                    t[i][j] = max(t[i][j], t[r][j] + t[i - r][j])

        return t[m][n]
