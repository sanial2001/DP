class Solution:
    def solve(self, nums, i, j, x, cnt, d):
        if x == 0:
            return cnt
        if i > j:
            return float("inf")
        if (i, j, x, cnt) in d:
            return d[(i, j, x, cnt)]
        x1 = self.solve(nums, i + 1, j, x - nums[i], cnt + 1, d)
        x2 = self.solve(nums, i, j - 1, x - nums[j], cnt + 1, d)
        d[(i, j, x, cnt)] = min(x1, x2)
        return d[(i, j, x, cnt)]

    def minOperations(self, nums: List[int], x: int) -> int:
        ans = self.solve(nums, 0, len(nums) - 1, x, 0, {})
        return -1 if ans == float("inf") else ans
