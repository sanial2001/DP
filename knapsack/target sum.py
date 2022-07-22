class Solution:
    def solve(self, nums, i, sums, target):
        if i == len(nums):
            if sums == target:
                return 1
            return 0
        x = self.solve(nums, i + 1, sums + nums[i], target)
        y = self.solve(nums, i + 1, sums - nums[i], target)
        return x + y

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.solve(nums, 0, 0, target)


class Solution:
    def solve(self, nums, i, sums, target):
        if i == len(nums):
            if sums == target:
                return 1
            return 0
        if (i, sums) in self.d:
            return self.d[(i, sums)]
        x = self.solve(nums, i + 1, sums + nums[i], target)
        y = self.solve(nums, i + 1, sums - nums[i], target)
        self.d[(i, sums)] = x + y
        return self.d[(i, sums)]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.d = {}
        return self.solve(nums, 0, 0, target)


