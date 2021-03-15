"""Coin Change"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #### Practice:
        dp = [0] + [float('inf')]*amount
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i-coin]+1)
        return -1 if dp[amount]==float('inf') else dp[-1]
    
        ## R2:
        dp = [0]+[float('inf')]*amount

        for i in range(1, amount+1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i-coin]+1)

        return -1 if dp[amount] == float('inf') else dp[amount]
