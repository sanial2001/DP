class Solution:
    def lislength(self, nums):
        lis = [nums[0]]
        for num in nums[1:]:
            if num > lis[-1]:
                lis.append(num)
            else:
                index = bisect_left(lis, num)
                lis[index] = num
        return len(lis)

    def minOperations(self, target: List[int], arr: List[int]) -> int:
        d = {num: i for i, num in enumerate(target)}
        nums = []
        for val in arr:
            if val in d:
                nums.append(d[val])

        if not nums:
            return len(target)
        return len(target) - self.lislength(nums)
