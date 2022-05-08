class Solution:
    def dfs(self, grid, row, col, d):
        if row == len(grid) - 1 and col == len(grid[0]) - 1:
            return (grid[row][col], grid[row][col])
        if row == len(grid) or col == len(grid[0]):
            return (float("-inf"), float("inf"))
        if grid[row][col] == 0:
            return (0, 0)
        if (row, col) in d:
            return d[(row, col)]
        mx1, mn1 = self.dfs(grid, row + 1, col, d)
        mx2, mn2 = self.dfs(grid, row, col + 1, d)
        mx = max(mx1, mx2) * grid[row][col]
        mn = min(mn1, mn2) * grid[row][col]
        d[(row, col)] = (mx, mn) if grid[row][col] > 0 else (mn, mx)
        return d[(row, col)]

    def maxProductPath(self, grid: List[List[int]]) -> int:
        d = {}
        mx, _ = self.dfs(grid, 0, 0, d)
        return mx % (10 ** 9 + 7) if mx >= 0 else -1
