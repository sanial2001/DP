class Solution:
    def solve(self, start, end):
        if start >= end:
            return 0
        if (start, end) in self.d:
            return self.d[(start, end)]
        self.d[(start, end)] = float("inf")
        for i in range(start, end + 1):
            cost1 = self.solve(start, i - 1) + i
            cost2 = self.solve(i + 1, end) + i
            cost = max(cost1, cost2)
            self.d[(start, end)] = min(self.d[(start, end)], cost)
        return self.d[(start, end)]

    def getMoneyAmount(self, n: int) -> int:
        self.d = {}
        return self.solve(1, n)
