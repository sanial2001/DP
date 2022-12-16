class Solution:
    def solve(self, t, row, col, k):
        if t[row][col] == 0:
            return 0
        if k == 1:
            return 1
        if (row, col, k) in self.d:
            return self.d[(row, col, k)]
        res = 0
        for i in range(row + 1, len(t)):
            if t[row][col] - t[i][col] > 0:
                res += self.solve(t, i, col, k - 1)
        for j in range(col + 1, len(t[0])):
            if t[row][col] - t[row][j] > 0:
                res += self.solve(t, row, j, k - 1)
        self.d[(row, col, k)] = res
        return self.d[(row, col, k)] % (10 ** 9 + 7)

    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])
        t = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        self.d = {}
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if pizza[i][j] == "A":
                    t[i][j] = t[i + 1][j] + t[i][j + 1] - t[i + 1][j + 1] + 1
                else:
                    t[i][j] = t[i + 1][j] + t[i][j + 1] - t[i + 1][j + 1]

        return self.solve(t, 0, 0, k)
