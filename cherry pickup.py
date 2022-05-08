class Solution:
    def solve(self, grid, r1, c1, r2, c2, t):
        if r1 == len(grid) or c1 == len(grid[0]) or r2 == len(grid) or c2 == len(grid[0]) or grid[r1][c1] == -1 or grid[r2][c2] == -1:
            return -1000

        if r1 == len(grid)-1 and c1 == len(grid[0])-1:
            return grid[r1][c1]

        if t[r1][c1][r2][c2] != 0:
            return t[r1][c1][r2][c2]

        count = 0
        if r1 == r2 and c1 == c2:
            count += grid[r1][c1]
        else:
            count = count + grid[r1][c1] + grid[r2][c2]

        x1 = self.solve(grid, r1 + 1, c1, r2, c2 + 1, t)
        x2 = self.solve(grid, r1 + 1, c1, r2 + 1, c2, t)
        x3 = self.solve(grid, r1, c1 + 1, r2, c2 + 1, t)
        x4 = self.solve(grid, r1, c1 + 1, r2 + 1, c2, t)

        temp = max(x1, x2, x3, x4)
        t[r1][c1][r2][c2] = temp + count
        return temp + count

    def cherryPickup(self, grid) -> int:
        n = len(grid)
        t = [[[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)]
        print(self.solve(grid, 0, 0, 0, 0, t))


if __name__ == '__main__':
    grid = [[0,1,-1],[1,0,-1],[1,1,1]]
    Solution().cherryPickup(grid)
