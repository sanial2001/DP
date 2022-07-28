class Solution:
    def solve(self, nums):
        if not nums:
            return 0

        n = len(nums)
        pre, suf = [1] * n, [1] * n

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                pre[i] = pre[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                suf[i] = suf[i + 1] + 1

        ans = max(max(pre), max(suf))

        for i in range(1, n - 1):
            if nums[i + 1] > nums[i - 1]:
                ans = max(ans, pre[i - 1] + suf[i + 1])

        return ans
