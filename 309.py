"""Best Time to Buy and Sell Stock with Cooldown"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ########### Practice
        if not prices:
            return 0
        A = 0
        B = -prices[0]
        C = 0

        for price in prices:
            tmp = A
            A = max(A, C)
            B = max(B, tmp - price)
            C = B + price

        return max(A, C)


        # R2:
        if len(prices) < 2:
            return 0
        A = 0
        B = -prices[0]
        C = 0

        for price in prices:
            tmp = A
            A = max(A, C)
            C = B + price # old B before new B
            B = max(tmp - price, B) # tmp is old A
        return max(A, C) # final state needs to be max of A and C


























        # R1:
        sell, buy, prev_buy, prev_sell = 0, -price[0], 0, 0

        for price in prices:
            prev_buy = buy
            buy = max(prev_sell-price, prev_buy)
            prev_sell = sell
            sell = max(prev_buy+price, prev_sell)
        return sell
