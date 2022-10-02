from functools import lru_cache


class Solution:
    @lru_cache
    def solve(self, nums, index, path, prev):
        if len(path) > self.mx:
            self.ans = path.copy()
            self.mx = len(path)
        for i in range(index, len(nums)):
            if nums[i] % prev == 0:
                self.solve(nums, i + 1, path + [nums[i]], nums[i])

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        self.ans, self.mx = [], 0
        self.solve(nums, 0, [], 1)
        return self.ans
