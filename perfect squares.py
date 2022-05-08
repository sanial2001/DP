import math


class Solution:
    def numSquares_tle(self, n: int) -> int:
        t = [1 for _ in range(n + 1)]
        t[0], t[1] = 0, 1

        for i in range(2, n + 1):
            if math.ceil(math.sqrt(i)) == math.floor(math.sqrt(i)):
                t[i] = 1
                continue
            ans = 100000
            for j in range(1, i // 2 + 1):
                ans = min(ans, t[i - j] + t[j])
            t[i] = ans
        # print(t)

        return t[n]

    def numSquares(self, n: int) -> int:
        t = [i for i in range(n+1)]

        for i in range(2, n+1):
            k = 1
            ans = 100000
            while i-(k*k) >= 0:
                ans = min(ans, t[i-(k*k)]+1)
                k = k+1
            t[i] = ans

        print(t[n])


if __name__ == '__main__':
    Solution().numSquares(36)
