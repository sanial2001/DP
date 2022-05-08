class Solution:
    def maxProfit(self, prices):
        profit, buy, sell = 0, prices[0], prices[0]
        for i in range(1, len(prices)):
            if prices[i] < prices[i-1]:
                profit = profit + (sell-buy)
                buy, sell = prices[i], prices[i]
            else:
                sell = prices[i]
        if sell > buy:
            profit = profit + (sell-buy)
        print(profit)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    Solution().maxProfit(arr)
