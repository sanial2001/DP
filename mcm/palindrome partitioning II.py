class Solution:
    def minCut(self, str: str) -> int:
        '''
        n = len(s)
        t = [[100000 for _ in range(n)] for _ in range(n)]

        for g in range(n):
            i = 0
            for j in range(g, n):
                if g == 0:
                    t[i][j] = 0
                elif g == 1:
                    t[i][j] = 0 if s[i] == s[j] else 1
                else:
                    if s[i] == s[j] and t[i+1][j-1] == 0:
                        t[i][j] = 0
                    else:
                        for k in range(i, j):
                            t[i][j] = min(t[i][j], 1+t[i][k]+t[k+1][j])
                i = i+1

        return t[0][n-1]
        '''
        n = len(str)

        bool_t = [[-1 for _ in range(n)] for _ in range(n)]
        for g in range(n):
            i = 0
            for j in range(g, n):
                if g == 0:
                    bool_t[i][j] = True
                elif g == 1:
                    if str[i] == str[j]:
                        bool_t[i][j] = True
                    else:
                        bool_t[i][j] = False
                else:
                    if str[i] == str[j] and bool_t[i + 1][j - 1] == True:
                        bool_t[i][j] = True
                    else:
                        bool_t[i][j] = False
                i = i + 1

        t = [-1 for _ in range(n)]
        t[0] = 0

        for j in range(1, n):
            if bool_t[0][j]:
                t[j] = 0
            else:
                i = j
                min_val = 10000
                while i >= 1:
                    if bool_t[i][j]:
                        min_val = min(min_val, t[i - 1])
                    i = i - 1
                t[j] = min_val + 1

        return t[n - 1]
