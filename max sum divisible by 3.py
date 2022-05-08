class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        t = [0, 0, 0]
        for num in nums:
            temp = t[:]
            for i in range(3):
                sums = temp[i] + num
                t[sums % 3] = max(sums, t[sums % 3])
        return t[0]
