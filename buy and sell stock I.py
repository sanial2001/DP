class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell, profit = prices[0], 0
        for i in range(1, len(prices)):
            if prices[i] < sell:
                sell = prices[i]
            profit = max(profit, prices[i] - sell)
        return profit
