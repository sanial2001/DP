class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        t = [[True for _ in range(n+1)] for _ in range(m+1)]

        for i in range(n-1, -1, -1):
            t[m][i] = False
        for i in range(m-1, -1, -1):
            if p[i] == '*':
                t[i][n] = t[i+1][n]
            else:
                t[i][n] = False

        for i in range(m-1, -1, -1):
            val = t[i+1][n]
            for j in range(n-1, -1, -1):
                if p[i].isalpha():
                    if p[i] == s[j]:
                        t[i][j] = t[i+1][j+1]
                    else:
                        t[i][j] = False
                elif p[i] == '?':
                    t[i][j] = t[i+1][j+1]
                else:
                    val = val or t[i+1][j]
                    t[i][j] = val

        for i in t:
            print(i)


if __name__ == '__main__':
    s = "baaabab"
    p = "ba*a?"
    Solution().isMatch(s, p)

