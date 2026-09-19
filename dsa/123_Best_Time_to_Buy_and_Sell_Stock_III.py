class Solution(object):
    def maxProfit(self, prices):
        buy1 = prices[0]
        profit1 = 0

        buy2 = prices[0]
        profit2 = 0

        for i in range(1, len(prices)):

            # First transaction
            if prices[i] < buy1:
                buy1 = prices[i]

            else:
                profit1 = max(profit1, prices[i] - buy1)

            # Second transaction
            if prices[i] - profit1 < buy2:
                buy2 = prices[i] - profit1

            else:
                profit2 = max(profit2, prices[i] - buy2)

        return profit2