class Solution:
    def dfs(self, m, n, row, col, move):
        if move < 0:
            return 0
        if row < 0 or col < 0 or row == m or col == n:
            return 1
        if (row, col, move) in self.dp:
            return self.dp[(row, col, move)]
        t = self.dfs(m, n, row - 1, col, move - 1)
        l = self.dfs(m, n, row, col - 1, move - 1)
        d = self.dfs(m, n, row + 1, col, move - 1)
        r = self.dfs(m, n, row, col + 1, move - 1)
        self.dp[(row, col, move)] = t + l + d + r
        return self.dp[(row, col, move)] % (10 ** 9 + 7)

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        self.dp = {}
        return self.dfs(m, n, startRow, startColumn, maxMove)
