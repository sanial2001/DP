class Solution:
    def solve(self, nums) -> int:
        n = len(nums)
        t = [[0 for _ in range(n)] for _ in range(2)]
        t[0][0] = nums[0]

        for i in range(1, n):
            t[0][i] = t[1][i - 1] + nums[i]
            t[1][i] = max(t[0][i - 1], t[1][i - 1])

        return max(t[0][n - 1], t[1][n - 1])

    def rob(self, nums) -> int:
        print(max(self.solve(nums[:-1]), self.solve(nums[1:])))


if __name__ == '__main__':
    arr = [1, 2]
    Solution().rob(arr)
