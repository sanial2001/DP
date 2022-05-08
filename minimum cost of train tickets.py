class Solution:
    def find(self, days, i, target):
        while i < len(days) and days[i] <= target:
            i = i + 1
        return i

    def solve(self, days, costs, i, d):
        if i >= len(days):
            return 0
        if i in d:
            return d[i]
        x1 = self.solve(days, costs, i + 1, d) + costs[0]
        index = self.find(days, i, days[i] + 6)
        x2 = self.solve(days, costs, index, d) + costs[1]
        index = self.find(days, i, days[i] + 29)
        x3 = self.solve(days, costs, index, d) + costs[2]
        d[i] = min(x1, x2, x3)
        return d[i]

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        return self.solve(days, costs, 0, {})
