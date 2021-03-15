class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ### Practice:
        if not prices:
            return 0
        A = 0
        B = float('-inf')
        for price in prices:
            A = max(A, B + price)
            B = max(B, -price)
        return A 
        ## R2:
        A = 0
        B = float('-inf') # to be safe: to aviod if prices is empty []

        for price in prices:
            tmp = A
            A = max(B + price, A)
            B = max(B, - price)

        return A
        # R1:
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min (min_price, price)
            profit = price - min_price
            max_profit = max (max_profit, profit)

        return max_profit
