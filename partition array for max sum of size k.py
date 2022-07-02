class Solution:
    def solve(self, nums, index, k):
        if index == len(nums):
            return 0
        if index in self.d:
            return self.d[index]
        res = 0
        max_num = 0
        for i in range(index, min(len(nums), index + k)):
            max_num = max(max_num, nums[i])
            max_fill = max_num * (i - index + 1)
            rem = max_fill + self.solve(nums, i + 1, k)
            res = max(res, rem)
            self.d[index] = res
        return res

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        self.d = {}
        return self.solve(arr, 0, k)
