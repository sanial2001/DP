class Solution:
    def solve(self, group, profit, i, sums, cnt, n, minProfit):
        if i == 0:
            if sums >= minProfit and cnt <= n:
                return 1
            return 0
        if group[i - 1] <= n:
            return self.solve(group, profit, i - 1, sums + profit[i - 1], cnt + group[i - 1], n,
                              minProfit) + self.solve(group, profit, i - 1, sums, cnt, n, minProfit)
        else:
            return self.solve(group, profit, i - 1, sums, cnt, n, minProfit)

    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        return self.solve(group, profit, len(profit), 0, 0, n, minProfit)


class SolutionMemo:
    def solve(self, group, profit, i, sums, cnt, n, minProfit):
        if cnt > n:
            return 0
        if i == 0:
            if sums >= minProfit and cnt <= n:
                return 1
            return 0
        if (i, sums, cnt) in self.d:
            return self.d[(i, sums, cnt)]
        if group[i - 1] <= n:
            self.d[(i, sums, cnt)] = self.solve(group, profit, i - 1, sums + profit[i - 1], cnt + group[i - 1], n,
                                                minProfit) + self.solve(group, profit, i - 1, sums, cnt, n, minProfit)
            return self.d[(i, sums, cnt)] % (10 ** 9 + 7)
        else:
            self.d[(i, sums, cnt)] = self.solve(group, profit, i - 1, sums, cnt, n, minProfit)
            return self.d[(i, sums, cnt)] % (10 ** 9 + 7)

    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        self.d = {}
        return self.solve(group, profit, len(profit), 0, 0, n, minProfit)
