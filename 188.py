"""188. Best Time to Buy and Sell Stock IV"""

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k >= len(prices)/2:
            A = 0
            B = float('-inf')

            for price in prices:
                tmp = A
                A = max(A, B + price)
                B = max(B, tmp - price)

            return A

        A_dp = [0]*(k+1)
        B_dp = [float('-inf')]*(k+1)


        for price in prices:
            for i in range(k, 0, -1):

                A_dp[i] = max(A_dp[i], B_dp[i] + price)
                B_dp[i] = max(B_dp[i], A_dp[i-1] - price)

        return A_dp[k]

2
[6,1,3,2,4,7]

s = Solution()
s.maxProfit(2, [3,2,6,5,0,3])
print(s.maxProfit(2, [3,2,6,5,0,3]))
