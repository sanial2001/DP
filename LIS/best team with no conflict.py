class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        nums = list(zip(ages, scores))
        nums.sort()
        # print(nums)
        t = [0 for _ in range(n)]
        t[0] = nums[0][1]

        for i in range(1, n):
            j = i - 1
            temp = []
            while j >= 0:
                if nums[i][1] >= nums[j][1]:
                    temp.append(t[j])
                j -= 1
            if not temp:
                t[i] = nums[i][1]
            else:
                t[i] = max(temp) + nums[i][1]

        return max(t)
