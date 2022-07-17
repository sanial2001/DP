class Solution:
    def rob(self, nums):
        n = len(nums)
        t = [[0 for _ in range(n)] for _ in range(2)]
        t[0][0] = nums[0]
        for j in range(1, n):
            t[0][j] = t[1][j - 1] + nums[j]
            t[1][j] = max(t[0][j - 1], t[1][j - 1])
        return max(t[0][n - 1], t[1][n - 1])

    def helper(self, matrix, row):
        if row >= len(matrix):
            return 0
        if row in self.d:
            return self.d[row]
        self.d[row] = 0
        take = self.helper(matrix, row + 2) + self.rob(matrix[row])
        not_taken = self.helper(matrix, row + 1)
        self.d[row] = max(self.d[row], max(take, not_taken))
        return self.d[row]

    def solve(self, matrix):
        self.d = {}
        return self.helper(matrix, 0)
