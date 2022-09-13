class Solution:
    def solve(self, ratings, ages):
        nums = list(zip(ages, ratings))
        nums.sort()
        n = len(nums)
        t = [nums[i][1] for i in range(n)]

        for i in range(n):
            for j in range(i):
                if nums[i][1] >= nums[j][1] and t[j] + nums[i][1] >= t[i]:
                    t[i] = t[j] + nums[i][1]

        return max(t)
