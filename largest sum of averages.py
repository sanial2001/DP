class Solution:
    def solve(self, nums, index, k):
        if index == len(nums) - 1 or k == 1:
            return sum(nums[index:]) / (len(nums) - index)
        if (index, k) in self.d:
            return self.d[(index, k)]
        self.d[(index, k)] = float("-inf")
        for i in range(index, len(nums) - k + 1):
            curr = sum(nums[index:i + 1]) / (i - index + 1) + self.solve(nums, i + 1, k - 1)
            self.d[(index, k)] = max(self.d[(index, k)], curr)
        return self.d[(index, k)]

    def largestSumOfAverages(self, nums, k: int) -> float:
        self.d = {}
        return self.solve(nums, 0, k)
