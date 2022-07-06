class Solution:
    def dp(self, s):
        n = len(s)
        t = [[0 for _ in range(n)] for _ in range(n)]
        ans = 0
        for g in range(n):
            i = 0
            for j in range(g, n):
                if g == 0:
                    t[i][j] = 1
                    ans = 1
                elif g == 1:
                    if s[i] == s[j]:
                        t[i][j] = 1
                        ans = 2
                else:
                    if s[i] == s[j] and t[i + 1][j - 1] == 1:
                        t[i][j] = 1
                        ans = max(ans, j - i + 1)
                i += 1
        return ans

    def solve(self, s):
        m = len(s)
        s += s
        n = len(s)
        i, j = 0, m
        ans = 0
        while j < n:
            word = s[i:j]
            ans = max(ans, self.dp(word))
            i, j = i + 1, j + 1
        return ans
