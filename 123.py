"""123. Best Time to Buy and Sell Stock III"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ######## Practice:
        if not prices:
            return 0

        A_dp = [0]*(2+1)
        B_dp = [float('-inf')]*(2+1)

        for price in prices:
            for i in range(2, 0, -1):

                A_dp[i] = max(A_dp[i], B_dp[i] + price)
                B_dp[i] = max(B_dp[i], A_dp[i-1] - price)

        return A_dp[2]

        #############
        A0 = 0
        B0 = float('-inf')
        A1 = 0
        B1= float('-inf')

        for price in prices:
            tmp1 = A0
            A1 = max(A1, B1 + price)
            B1 = max(B1, tmp1 - price)

            A0 = max(B0 + price, A0)
            B0 = max(B0, - price)

        return A1
