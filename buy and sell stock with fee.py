class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        t = [[0 for _ in range(2)] for _ in range(n)]
        t[0][0], t[0][1] = -prices[0], 0

        for i in range(1, n):
            t[i][0] = max(t[i - 1][0], t[i - 1][1] - prices[i])
            t[i][1] = max(t[i - 1][1], t[i - 1][0] + prices[i] - fee)

        return max(t[n - 1])
