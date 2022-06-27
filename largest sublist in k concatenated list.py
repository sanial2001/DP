class Solution:
    def kadane(self, nums):
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(max(nums), 0)

    def solve(self, nums, k):
        if k == 0 or not nums:
            return 0
        sums = sum(nums)
        if k == 1:
            return self.kadane(nums)
        if sums > 0:
            return self.kadane(nums + nums) + (k - 2) * sums
        else:
            return self.kadane(nums + nums)
