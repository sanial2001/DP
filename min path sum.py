class Solution:
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        t = [[-1 for _ in range(n)] for _ in range(m)]
        t[m-1][n-1] = grid[m-1][n-1]

        for i in range(n-2, -1, -1):
            t[m-1][i] = t[m-1][i+1] + grid[m-1][i]
        for i in range(m-2, -1, -1):
            t[i][n-1] = t[i+1][n-1] + grid[i][n-1]

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                t[i][j] = grid[i][j] + min(t[i][j+1], t[i+1][j])

        #for val in t:
        #    print(val)

        print(t[0][0])


if __name__ == '__main__':
    grid = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
    Solution().minPathSum(grid)
