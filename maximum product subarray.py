class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxp, minp, ans = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            x = max(nums[i], maxp * nums[i], minp * nums[i])
            y = min(nums[i], maxp * nums[i], minp * nums[i])
            maxp, minp = x, y
            ans = max(ans, maxp)
        return ans
