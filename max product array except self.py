class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1 for _ in range(n + 2)]
        suffix = [1 for _ in range(n + 2)]

        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for i in range(n, 0, -1):
            suffix[i] = suffix[i + 1] * nums[i - 1]

        ans = []
        for i in range(1, n + 1):
            ans.append(prefix[i - 1] * suffix[i + 1])

        return ans
