class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        t = [[False for _ in range(n)] for _ in range(n)]

        for g in range(n):
            i = 0
            for j in range(g, n):
                if g == 0:
                    t[i][j] = True
                elif g == 1 and s[i] == s[j]:
                    t[i][j] = True
                else:
                    if s[i] == s[j] and t[i + 1][j - 1] == True:
                        t[i][j] = True
                i += 1

        for cut1 in range(n - 2):
            for cut2 in range(cut1 + 1, n - 1):
                # print(cut1, cut2)
                left = t[0][cut1]
                mid = t[cut1 + 1][cut2]
                right = t[cut2 + 1][n - 1]
                if left and mid and right:
                    return True

        return False
