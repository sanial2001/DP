class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        profit, buy, sell = [], prices[0], prices[0]
        for i in range(1, n):
            if prices[i] <= prices[i - 1]:
                profit.append(sell - buy)
                buy, sell = prices[i], prices[i]
            else:
                sell = prices[i]
        if sell > buy:
            profit.append(sell - buy)

        profit.sort()
        print(profit)
        print(profit[-1] + profit[-2])


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    Solution().maxProfit(arr)