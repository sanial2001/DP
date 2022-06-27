from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [nums[0]]
        for num in nums[1:]:
            if lis and num > lis[-1]:
                lis.append(num)
            else:
                index = bisect_left(lis, num)
                lis[index] = num
        return len(lis)
