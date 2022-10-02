class Solution:
    def helper(self, x, y, m, n):
        if n == 0 or (m == 0 and n == 0):
            return 1
        if m == 0:
            return 0
        if (m, n) in self.d:
            return self.d[(m, n)]
        if x[m - 1] == y[n - 1]:
            self.d[(m, n)] = (self.helper(x, y, m - 1, n - 1) + self.helper(x, y, m - 1, n)) % (10 ** 9 + 7)
            return self.d[(m, n)]
        else:
            self.d[(m, n)] = self.helper(x, y, m - 1, n) % (10 ** 9 + 7)
            return self.d[(m, n)]

    def solve(self, s, t):
        if len(s) == 0 or len(t) == 0:
            return 0
        self.d = {}
        return self.helper(s, t, len(s), len(t))
