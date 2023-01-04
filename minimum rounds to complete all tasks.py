class Solution:
    def solve(self, n):
        if n == 1 or n < 0:
            return float("inf")
        elif n == 0:
            return 0
        if n in self.memo:
            return self.memo[n]
        self.memo[n] = min(self.solve(n - 2), self.solve(n - 3)) + 1
        return self.memo[n]

    def minimumRounds(self, tasks: List[int]) -> int:
        d = collections.defaultdict(int)
        for task in tasks:
            d[task] += 1

        res = 0
        self.memo = {}
        for key in d:
            res += self.solve(d[key])

        # print(res)
        return res if res != float("inf") else -1
