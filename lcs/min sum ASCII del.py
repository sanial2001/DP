class Solution:
    def solve(self, x, y, m, n):
        if m == 0 or n == 0:
            if m == 0 and n == 0:
                return 0
            elif m == 0:
                s = 0
                for i in range(n):
                    s += ord(y[i])
                return s
            elif n == 0:
                s = 0
                for i in range(m):
                    s += ord(x[i])
                return s
        if x[m-1] == y[n-1]:
            return self.solve(x, y, m-1, n-1)
        else:
            return min(ord(y[n-1]) + self.solve(x, y, m, n-1), ord(x[m-1]) + self.solve(x, y, m-1, n))

    def dp(self, x, y, M, N):
        t = [[0 for _ in range(N+1)] for _ in range(M+1)]
        for i in range(M+1):
            for j in range(N+1):
                if i == 0 and j == 0:
                    t[i][j] = 0
                elif j == 0:
                    t[i][j] = t[i-1][j] + ord(x[i-1])
                elif i == 0:
                    t[i][j] = t[i][j-1] + ord(y[j-1])

        for m in range(1, M+1):
            for n in range(1, N+1):
                if x[m-1] == y[n-1]:
                    t[m][n] = t[m-1][n-1]
                else:
                    t[m][n] = min(ord(y[n-1]) + t[m][n-1],
                                  ord(x[m-1]) + t[m-1][n])

        for val in t:
            print(val)


    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        self.dp(s1, s2, len(s1), len(s2))


if __name__ == '__main__':
    s1 = 'abcde'
    s2 = 'ace'
    Solution().minimumDeleteSum(s1, s2)
