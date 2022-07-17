class Solution:
    def helper(self, nums, sums, index, k):
        if sums >= k:
            if sums == k:
                return True
            return False
        if index >= len(nums):
            return False
        if (sums, index) in self.d:
            return self.d[(sums, index)]
        self.d[(sums, index)] = self.helper(nums, sums + nums[index], index + 2, k) or self.helper(nums, sums,
                                                                                                   index + 1, k)
        return self.d[(sums, index)]

    def solve(self, nums, k):
        self.d = {}
        return self.helper(nums, 0, 0, k)
