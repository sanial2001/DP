class Solution:
    def helper(self, n):
        if n == 0:
            return False
        i = 1
        if n in self.d:
            return self.d[n]
        while i * i <= n:
            if not self.helper(n - i * i):
                self.d[n] = True
                return self.d[n]
            i += 1
        self.d[n] = False
        return self.d[n]

    def solve(self, n):
        self.d = {}
        return self.helper(n)
