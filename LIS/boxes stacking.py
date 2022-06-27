class Solution:
    def solve(self, matrix):
        matrix.sort()
        nums = [x[1] for x in matrix]
        n = len(nums)
        t = [1 for _ in range(n)]

        for i in range(len(nums)):
            j = i - 1
            temp = []
            while j >= 0:
                if nums[j] < nums[i] and matrix[j][0] != matrix[i][0]:
                    temp.append(t[j])
                j -= 1
            if temp: t[i] = max(temp) + 1

        # print(t)

        return max(t)
