class Solution:
    def subset_sum(self, arr, N, S):
        t = [[-1 for _ in range(S + 1)] for _ in range(N + 1)]

        for i in range(N + 1):
            t[i][0] = 1
        for i in range(1, S + 1):
            t[0][i] = 0

        for n in range(1, N + 1):
            for s in range(1, S + 1):
                if arr[n - 1] == 0:
                    t[n][s] = t[n - 1][s]
                elif arr[n - 1] > s:
                    t[n][s] = t[n - 1][s]
                else:
                    t[n][s] = t[n - 1][s - arr[n - 1]] + t[n - 1][s]

        return t[N][S]

    def findTargetSumWays(self, nums, target) -> int:
        n = len(nums)
        sum_ele = sum(nums)
        if target > sum_ele:
            return 0
        if (target + sum_ele) % 2 != 0:
            return 0
        s = (target + sum_ele) // 2
        res = self.subset_sum(nums, n, s)

        cnt = 0
        for i in range(n):
            if nums[i] == 0:
                cnt += 1

        return pow(2, cnt) * res


if __name__ == '__main__':
    info = {
        'arr': [100],
        'diff': -200
    }
    print(Solution().findTargetSumWays(info['arr'], info['diff']))
