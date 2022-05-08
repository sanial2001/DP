class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        t = [float("inf") for _ in range(n)]
        t[n - 1] = 0
        for i in range(n - 2, -1, -1):
            if nums[i] != 0:
                start = i + 1
                end = min(n - 1, i + nums[i])
                temp = min(t[start:end + 1])
                t[i] = temp + 1
        return 0 if t[0] == float("inf") else t[0]


if __name__ == '__main__':
    nums = [3, 2, 1, 0, 4]
    Solution().canJump(nums)
