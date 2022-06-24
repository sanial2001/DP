class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        t = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
        t[0][0] = True

        for j in range(1, n + 1):
            t[0][j] = False

        for i in range(1, m + 1):
            if p[i - 1] == '*':
                t[i][0] = t[i - 2][0]
            else:
                t[i][0] = False

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[i - 1].isalpha():
                    if p[i - 1] == s[j - 1]:
                        t[i][j] = t[i - 1][j - 1]
                    else:
                        t[i][j] = False
                elif p[i - 1] == '.':
                    t[i][j] = t[i - 1][j - 1]
                elif p[i - 1] == '*':
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        t[i][j] = t[i - 2][j] or t[i][j - 1]
                    else:
                        t[i][j] = t[i - 2][j]

        return t[m][n]
