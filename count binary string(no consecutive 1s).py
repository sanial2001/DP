class Solution:
    def findIntegers(self, n: int) -> int:
        t = [[-1 for _ in range(n)] for _ in range(2)]
        t[0][0], t[1][0] = 1, 1
        for i in range(1, n):
            t[0][i] = t[0][i-1] + t[1][i-1]
            t[1][i] = t[0][i-1]
        return t[0][n-1] + t[1][n-1]


if __name__ == '__main__':
    print(Solution().findIntegers(5))
