"""122. Best Time to Buy and Sell Stock II (Easy)"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #### Practice:
        if not prices:
            return 0
        A = 0
        B = float('-inf')

        for price in prices:
            tmp = A
            A = max(A, B + price)
            B = max(B, tmp - price)

        return A 
        ## R2:
        A = 0
        B = -prices[0]

        for price in prices:
            tmp = A
            A = max(B + price, A)
            B = max(B, tmp - price)

        return A

        ## R1:
        max_profit = 0
        price_prev = prices[0]
        for price in prices:
            if price - price_prev > 0:
                max_profit += (price - price_prev)
            price_prev = price


        return max_profit
