class Solution:
    def maxPalindromes(self, s: str, l: int) -> int:
        n = len(s)
        t = [[[0, 0] for _ in range(n)] for _ in range(n)]

        for g in range(n):
            i = 0
            for j in range(g, n):
                if g == 0:
                    t[i][j][1] = 1
                elif g == 1:
                    if s[i] == s[j]:
                        t[i][j][1] = 1
                else:
                    if s[i] == s[j] and t[i + 1][j - 1][1] == 1:
                        t[i][j][1] = 1
                if g >= l - 1:
                    temp = 0
                    for k in range(i, j):
                        temp = max(temp, t[i][k][0] + t[k + 1][j][0])
                    t[i][j][0] = max(t[i][j][1], temp)
                i += 1
        '''
        for val in t:
            print(val)
        '''
        return t[0][n - 1][0]
