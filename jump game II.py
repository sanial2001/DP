class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        t = [float("inf") for _ in range(n)]
        t[n - 1] = 0
        for i in range(n - 2, -1, -1):
            if nums[i] != 0:
                start = i + 1
                end = min(n - 1, i + nums[i])
                temp = min(t[start:end + 1])
                t[i] = temp + 1
        return t[0]
