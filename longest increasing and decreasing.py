class Solution:
    def solve(self, nums):
        n = len(nums)
        inc, dec = [1] * n, [1] * n
        prev = nums[0]

        for i in range(1, n):
            if nums[i] > prev:
                inc[i] = inc[i - 1] + 1
            prev = nums[i]

        prev = nums[-1]
        for i in range(n - 2, -1, -1):
            if nums[i] > prev:
                dec[i] = dec[i + 1] + 1
            prev = nums[i]

        ans = 0
        for i in range(n):
            if inc[i] > 1 and dec[i] > 1: ans = max(ans, inc[i] + dec[i] - 1)

        return ans
