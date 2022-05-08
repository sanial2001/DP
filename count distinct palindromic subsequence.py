class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        n = len(s)
        t = [[0 for _ in range(n)] for _ in range(n)]

        for g in range(n):
            i = 0
            for j in range(g, n):
                if g == 0:
                    t[i][j] = 1
                elif g == 1:
                    t[i][j] = 2
                else:
                    if s[i] != s[j]:
                        t[i][j] = t[i][j - 1] + t[i + 1][j] - t[i + 1][j - 1]
                    else:
                        if s[i:j + 1].count(s[i]) == 2:
                            t[i][j] = 2 * t[i + 1][j - 1] + 2
                        elif s[i:j + 1].count(s[i]) == 3:
                            t[i][j] = 2 * t[i + 1][j - 1] + 1
                        else:
                            temp = s[i + 1:j]
                            x = i + temp.index(s[i]) + 2
                            y = j - temp[::-1].index(s[i]) - 2
                            t[i][j] = 2 * t[i + 1][j - 1] - t[x][y]
                i = i + 1

        return t[0][n - 1] % (10 ** 9 + 7)
