class Solution:
    def dfs(self, n, row, col, moves):
        if row < 0 or col < 0 or row >= m or col >= n:
            return 0
        if moves == 0:
            return 1
        x1 = self.dfs(n, row - 2, col - 1, moves - 1)
        x2 = self.dfs(n, row - 1, col - 2, moves - 1)
        x3 = self.dfs(n, row + 1, col - 2, moves - 1)
        x4 = self.dfs(n, row + 2, col - 1, moves - 1)
        x5 = self.dfs(n, row + 2, col + 1, moves - 1)
        x6 = self.dfs(n, row + 1, col + 2, moves - 1)
        x7 = self.dfs(n, row - 1, col + 2, moves - 1)
        x8 = self.dfs(n, row - 2, col + 1, moves - 1)
        return (x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8) / 8

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        return self.dfs(n, row, column, k)


class Solution_memo:
    def dfs(self, n, row, col, moves):
        if row < 0 or col < 0 or row >= n or col >= n:
            return 0
        if moves == 0:
            return 1
        if (row, col, moves) in self.dp:
            return self.dp[(row, col, moves)]
        x1 = self.dfs(n, row - 2, col - 1, moves - 1)
        x2 = self.dfs(n, row - 1, col - 2, moves - 1)
        x3 = self.dfs(n, row + 1, col - 2, moves - 1)
        x4 = self.dfs(n, row + 2, col - 1, moves - 1)
        x5 = self.dfs(n, row + 2, col + 1, moves - 1)
        x6 = self.dfs(n, row + 1, col + 2, moves - 1)
        x7 = self.dfs(n, row - 1, col + 2, moves - 1)
        x8 = self.dfs(n, row - 2, col + 1, moves - 1)
        self.dp[(row, col, moves)] = (x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8) / 8
        return self.dp[(row, col, moves)]

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        self.dp = {}
        return self.dfs(n, row, column, k)
