class Solution:
    def solve(self, matrix, k):
        m, n = len(matrix), len(matrix[0])
        t = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                t[i][j] = matrix[i - 1][j - 1] + t[i - 1][j] + t[i][j - 1] - t[i - 1][j - 1]

        ans = 0
        for i in range(m + 1):
            for ii in range(i, m + 1):
                for j in range(n + 1):
                    for jj in range(j, n + 1):
                        sums = t[ii][jj] + t[i][j] - (t[i][jj] + t[ii][j])
                        if sums <= k:
                            ans = max(ans, sums)

        return ans
