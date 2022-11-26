from typing import List


class Solution:
    def solve(self, grid, move, row, col):
        m, n = len(grid), len(grid[0])
        if row == m - 1:
            return grid[row][col]
        if (row, col) in self.d:
            return self.d[(row, col)]
        self.d[(row, col)] = float("inf")
        for j in range(n):
            temp = self.solve(grid, move, row + 1, j) + move[grid[row][col]][j] + grid[row][col]
            self.d[(row, col)] = min(self.d[(row, col)], temp)
        return self.d[(row, col)]

    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.d = {}
        res = float("inf")
        for j in range(n):
            res = min(res, self.solve(grid, moveCost, 0, j))
        return res
