class Solution:
    def solve(self, nums, k):
        n = len(nums)
        t = [[-1 for _ in range(n)] for _ in range(n)]

        for g in range(n):
            i = 0
            for j in range(g, n):
                if g < k:
                    t[i][j] = sum(nums[i:j + 1])
                else:
                    if (g + 2) % k == 0:
                        temp = []
                        for p in range(k - 1, j + 1):
                            temp.append(2 * t[i][p] + t[p + 1][j])
                        t[i][j] = min(temp)
                i += 1

        return t[0][n - 1]