class Solution:
    def maxProfit(self, prices):
        low, profit, max_profit = prices[0], 0, 0
        for i in range(1, len(prices)):
            if prices[i] < low:
                low, profit = prices[i], 0
            else:
                profit = prices[i] - low
                max_profit = max(max_profit, profit)
        return max_profit


if __name__ == '__main__':
    arr = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(arr))
