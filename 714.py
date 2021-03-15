"""714. Best Time to Buy and Sell Stock with Transaction Fee"""

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        ######## Practice
        if not prices:
            return 0
        A = 0
        B = -prices[0]

        for price in prices:
            tmp = A
            A = max(A, B + price - fee)
            B = max(B, tmp - price)
        return A 

        # pay fee when sell
        if len(prices) < 2:
            return 0
        A = 0
        B = -prices[0] ### or simply put float('-inf')

        for price in prices:
            tmp = A
            A = max(B + price - fee, A)
            B = max(tmp - price, B)

        return A

        ## pay fee when buy
        if len(prices) < 2:
            return 0
        A = 0
        B = -prices[0]-fee ## different than the B above

        for price in prices:
            tmp = A
            A = max(B + price , A)
            B = max(tmp - price - fee, B)

        return A
