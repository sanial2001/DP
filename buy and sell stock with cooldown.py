class Solution_recursion:
    def solve(self, prices, index, opt):
        if index >= len(prices):
            return 0
        res = 0
        if opt == 0:
            buy = self.solve(prices, index + 1, 1) - prices[index]
            cool = self.solve(prices, index + 1, 0)
            res = max(buy, cool)
        else:
            sell = self.solve(prices, index + 2, 0) + prices[index]
            cool = self.solve(prices, index + 1, 1)
            res = max(sell, cool)
        return res

    def maxProfit(self, prices: List[int]) -> int:
        return self.solve(prices, 0, 0)


class Solution_memo:
    def solve(self, prices, index, opt):
        if index >= len(prices):
            return 0
        if (index, opt) in self.dp:
            return self.dp[(index, opt)]
        if opt == 0:
            buy = self.solve(prices, index + 1, 1) - prices[index]
            cool = self.solve(prices, index + 1, 0)
            self.dp[(index, opt)] = max(buy, cool)
        else:
            sell = self.solve(prices, index + 2, 0) + prices[index]
            cool = self.solve(prices, index + 1, 1)
            self.dp[(index, opt)] = max(sell, cool)
        return self.dp[(index, opt)]

    def maxProfit(self, prices: List[int]) -> int:
        self.dp = {}
        return self.solve(prices, 0, 0)
