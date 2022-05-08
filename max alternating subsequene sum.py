class Solution:
    def maxAlternatingSum(self, nums) -> int:
        n = len(nums)
        res = nums[0]
        for i in range(1, n):
            res = res + max(nums[i]-nums[i-1], 0)
        return res