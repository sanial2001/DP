from bisect import bisect_left


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


class Solution:
    def solve(self, matrix):
        matrix.sort(key=lambda x: (x[0], -x[1]))
        n = len(matrix)
        lis = [matrix[0][1]]

        for num in matrix[1:]:
            # print(lis, num[1])
            if lis and num[1] > lis[-1]:
                lis.append(num[1])
            else:
                idx = bisect_left(lis, num[1])
                lis[idx] = num[1]

        return len(lis)
