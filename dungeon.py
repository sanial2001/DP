class Solution:
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        t = [[-1 for _ in range(n)] for _ in range(m)]
        t[m-1][n-1] = abs(dungeon[m-1][n-1]) + 1

        for i in range(n-2, -1, -1):
            t[m-1][i] = max(t[m-1][i+1] - dungeon[m-1][i], 1)

        for i in range(m-2, -1, -1):
            t[i][n-1] = max(t[i+1][n-1] - dungeon[i][n-1], 1)

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                t[i][j] = max(min(t[i][j+1], t[i+1][j]) - dungeon[i][j], 1)

        for val in t:
            print(val)


if __name__ == '__main__':
    m = [[-3, 5]]
    Solution().calculateMinimumHP(m)