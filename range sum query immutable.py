class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i-1]
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        x1 = self.nums[right]
        x2 = 0 if left == 0 else self.nums[left-1]
        return x1-x2


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)