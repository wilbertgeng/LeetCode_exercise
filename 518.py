"""518. Coin Change 2"""

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        ## Practice:
        dp = [1] + [0]*amount
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        return dp[-1]

        ## R2:
        dp = [1] + [0]*amount

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i - coin]

        return dp[-1]

        ## R1:
        dp = [1] + [0]*(amount)

        for i in coins:
            for j in range(1, amount + 1):
                if j >= i:
                    dp[j] += dp[j - i]

        return dp[-1]
