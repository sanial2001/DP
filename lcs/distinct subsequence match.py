class Solution:
    def lcs(self, x, y, m, n):
        if n == 0:
            return 1
        if m == 0:
            return 0
        if x[m-1] == y[n-1]:
            return self.lcs(x, y, m-1, n-1) + self.lcs(x, y, m-1, n)
        else:
            return self.lcs(x, y, m-1, n)

    def dp(self, x, y, M, N):
        t = [[-1 for _ in range(N+1)] for _ in range(M+1)]
        for m in range(M+1):
            for n in range(N+1):
                if n == 0:
                    t[m][n] = 1
                elif m == 0:
                    t[m][n] = 0

        for m in range(1, M+1):
            for n in range(1, N+1):
                if x[m-1] == y[n-1]:
                    t[m][n] = t[m-1][n-1] + t[m-1][n]
                else:
                    t[m][n] = t[m-1][n]
        return t[M][N]

    def numDistinct(self, s: str, t: str) -> int:
        print(self.dp(s, t, len(s), len(t)))


if __name__ == '__main__':
    s = "babgbag"
    t = "bag"
    Solution().numDistinct(s, t)
