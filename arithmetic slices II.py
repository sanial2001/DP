from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, nums):
        n = len(nums)
        t = [defaultdict(int) for _ in range(n)]
        ans = 0

        for i in range(1, n):
            j = 0
            while j < i:
                diff = nums[i] - nums[j]
                ans += t[j][diff]
                t[i][diff] += t[j][diff] + 1
                j = j+1

        print(ans)


if __name__ == "__main__":
    Solution().numberOfArithmeticSlices(nums=[2, 4, 6, 8, 10])
