class Solution:
    def minScoreTriangulation(self, values) -> int:
        n = len(values)
        t = [[-1 for _ in range(n)] for _ in range(n)]

        for g in range(n):
            i = 0
            for j in range(g, n):
                if g == 0:
                    t[i][j] = 0
                elif g == 1:
                    t[i][j] = 0
                elif g == 2:
                    t[i][j] = values[i]*values[j]*values[i+1]
                else:
                    ans = float('inf')
                    for k in range(i+1, j):
                        temp = values[i]*values[k]*values[j] + t[i][k] + t[k][j]
                        ans = min(ans, temp)
                    t[i][j] = ans
                i = i+1

        for val in t:
            print(val)


if __name__ == '__main__':
    Solution().minScoreTriangulation([1,3,1,4,1,5])