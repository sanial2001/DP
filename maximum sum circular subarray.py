class Solution:
    def kadane_max(self, nums):
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)

    def kadane_min(self, nums):
        for i in range(1, len(nums)):
            if nums[i - 1] < 0:
                nums[i] += nums[i - 1]
        return min(nums)

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        x = self.kadane_max(nums[::])
        y = sum(nums) - self.kadane_min(nums[::])
        if y == 0:
            y = max(nums)
        return max(x, y)
