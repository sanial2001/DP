class Solution:
    def solve(self, triangle, index):
        if index == len(triangle):
            return 0
        res = 1000000000
        for val in triangle[index]:
            res = min(val + self.solve(triangle, index + 1), res)
        return res

    def dp(self, triangle):
        n = len(triangle)
        t = [0 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(len(triangle[i])):
                t[j] = triangle[i][j] + min(t[j], t[j + 1])
        return t[0]

    def minimumTotal(self, triangle) -> int:
        print(self.solve(triangle, 0))


if __name__ == '__main__':
    Solution().minimumTotal([[-10]])
