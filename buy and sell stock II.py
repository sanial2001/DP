class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, buy = 0, prices[0]
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += (prices[i] - buy)
                buy = prices[i]
            else:
                buy = prices[i]
        return profit
