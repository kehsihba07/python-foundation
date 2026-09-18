class Solution(object):
    def maxProfit(self, prices):
        buy=prices[0]
        profit=0
        for i in range(1,len(prices)):
            if prices[i]<buy:
                buy=prices[i]
            else:
                cur_profit=prices[i]-buy
                if cur_profit>profit:
                    profit=cur_profit
        return profit
        """
        :type prices: List[int]
        :rtype: int
        """
        