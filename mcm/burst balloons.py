class Solution:
    def maxCoins(self, nums) -> int:
        n = len(nums)

        t = [[0 for _ in range(n)] for _ in range(n)]

        for g in range(n):
            i = 0
            for j in range(g, n):
                temp = -10000
                for k in range(i, j + 1):
                    left = 0 if k == i else t[i][k - 1]
                    right = 0 if k == j else t[k + 1][j]
                    lt = 1 if i == 0 else nums[i - 1]
                    rt = 1 if j == n - 1 else nums[j + 1]
                    temp = max(temp, left + right + lt * nums[k] * rt)
                t[i][j] = temp
                i = i + 1

        return t[0][n - 1]


if __name__ == '__main__':
    nums = [3, 1, 5, 8]
    Solution().maxCoins(nums)
