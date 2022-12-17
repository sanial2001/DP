class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        left = [[0 for _ in range(n)] for _ in range(m)]
        top = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                left[i][j] = grid[i][j]
                top[i][j] = grid[i][j]

        for i in range(m):
            for j in range(1, n):
                if grid[i][j] == 1:
                    left[i][j] += left[i][j - 1]

        for j in range(n):
            for i in range(1, m):
                if grid[i][j] == 1:
                    top[i][j] += top[i - 1][j]

        res = 0
        for i in range(m):
            for j in range(n):
                mn = min(left[i][j], top[i][j])
                while mn > 0:
                    if left[i - mn + 1][j] >= mn and top[i][j - mn + 1] >= mn:
                        res = max(res, mn)
                        break
                    mn -= 1

        return res * res
