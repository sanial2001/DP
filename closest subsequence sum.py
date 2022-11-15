class Solution:
    # @lru_cache
    def solve(self, nums, i, sums, path, goal):
        if i == len(nums):
            # print(path, sums)
            self.res = min(self.res, abs(sums - goal))
            return
        self.solve(nums, i + 1, sums + nums[i], path + [nums[i]], goal)
        self.solve(nums, i + 1, sums, path, goal)

    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        self.res = float("inf")
        self.solve(nums, 0, 0, [], goal)
        return self.res


class solution:
    def solve(self, nums, i, val, sums):
        if i == len(nums):
            sums.append(val)
            return
        self.solve(nums, i + 1, val + nums[i], sums)
        self.solve(nums, i + 1, val, sums)

    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        sum1, sum2 = [], []
        self.solve(nums[:n // 2], 0, 0, sum1)
        self.solve(nums[n // 2:], 0, 0, sum2)

        sum2 = sorted(sum2)
        # print(sum1, sum2)
        n2 = len(sum2)
        ans = float("inf")
        for s in sum1:
            rem = goal - s
            i = bisect_left(sum2, rem)
            if i < n2:
                ans = min(ans, abs(rem - sum2[i]))
            if i > 0:
                ans = min(ans, abs(rem - sum2[i - 1]))
        return ans
