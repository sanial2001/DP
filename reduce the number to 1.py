class Solution:
    def solve(self, n):
        if n == 1:
            return 0
        if n in self.d:
            return self.d[n]
        if n % 2 == 0:
            self.d[n] = 1 + self.solve(n // 2)
            return self.d[n]
        else:
            self.d[n] = 1 + min(self.solve(n - 1), self.solve(n + 1))
            return self.d[n]

    def integerReplacement(self, n: int) -> int:
        self.d = {}
        return self.solve(n)
