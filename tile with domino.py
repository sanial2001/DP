class Solution:
    def numTilings(self, n: int) -> int:
        t = [-1 for _ in range(n)]
        t[0], t[1] = 1, 2

        for i in range(2, n):
            t[i] = t[i-1] + t[i-2]

        return t[n-1]


if __name__ == '__main__':
    print(Solution().numTilings(5))
