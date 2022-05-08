class Solution:
    def solve(self, prices, index, option, k):
        if index == len(prices) or k == 0:
            return 0
        res = 0
        if option == 0:
            buy = self.solve(prices, index + 1, 1, k) - prices[index]
            cool = self.solve(prices, index + 1, 0, k)
            res = max(buy, cool)
        if option == 1:
            sell = self.solve(prices, index + 1, 0, k - 1) + prices[index]
            cool = self.solve(prices, index + 1, 1, k)
            res = max(sell, cool)
        return res

    def maxProfit(self, k: int, prices: List[int]) -> int:
        return self.solve(prices, 0, 0, k)


class Solution:
    def solve(self, prices, index, option, k):
        if index == len(prices) or k == 0:
            return 0
        if (index, option, k) in self.dp:
            return self.dp[(index, option, k)]
        if option == 0:
            buy = self.solve(prices, index + 1, 1, k) - prices[index]
            cool = self.solve(prices, index + 1, 0, k)
            self.dp[(index, option, k)] = max(buy, cool)
        if option == 1:
            sell = self.solve(prices, index + 1, 0, k - 1) + prices[index]
            cool = self.solve(prices, index + 1, 1, k)
            self.dp[(index, option, k)] = max(sell, cool)
        return self.dp[(index, option, k)]

    def maxProfit(self, k: int, prices: List[int]) -> int:
        self.dp = {}
        return self.solve(prices, 0, 0, k)