class Solution:
    def solve(self, prices, index, option, trans):
        if index == len(prices) or trans == 0:
            return 0
        res = 0
        if option == 0:
            buy = self.solve(prices, index + 1, 1, trans) - prices[index]
            cool = self.solve(prices, index + 1, 0, trans)
            res = max(buy, cool)
        if option == 1:
            sell = self.solve(prices, index + 1, 0, trans - 1) + prices[index]
            cool = self.solve(prices, index + 1, 1, trans)
            res = max(sell, cool)
        return res

    def maxProfit(self, prices: List[int]) -> int:
        return self.solve(prices, 0, 0, 2)


class Solution_memo:
    def solve(self, prices, index, option, trans):
        if index == len(prices) or trans == 0:
            return 0
        if (index, option, trans) in self.dp:
            return self.dp[(index, option, trans)]
        if option == 0:
            buy = self.solve(prices, index + 1, 1, trans) - prices[index]
            cool = self.solve(prices, index + 1, 0, trans)
            self.dp[(index, option, trans)] = max(buy, cool)
        if option == 1:
            sell = self.solve(prices, index + 1, 0, trans - 1) + prices[index]
            cool = self.solve(prices, index + 1, 1, trans)
            self.dp[(index, option, trans)] = max(sell, cool)
        return self.dp[(index, option, trans)]

    def maxProfit(self, prices: List[int]) -> int:
        self.dp = {}
        return self.solve(prices, 0, 0, 2)
