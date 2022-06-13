class Solution:
    def solve(self, nums, index, d):
        if index == len(nums) or d == 1:
            # print(max(nums[index:]))
            return max(nums[index:])
        if (index, d) in self.d:
            return self.d[(index, d)]
        self.d[(index, d)] = float("inf")
        for i in range(index, len(nums) - d + 1):
            curr = max(nums[index:i + 1]) + self.solve(nums, i + 1, d - 1)
            self.d[(index, d)] = min(self.d[(index, d)], curr)
        return self.d[(index, d)]

    def minDifficulty(self, jobDifficulty, d: int) -> int:
        self.d = {}
        ans = self.solve(jobDifficulty, 0, d)
        if ans == float("inf"):
            return -1
        else:
            return ans
