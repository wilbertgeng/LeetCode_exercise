"""91. Decode Ways"""

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ## R3:
        n = len(s)
        dp = [0]*(n+1)
        if s[0] != "0":
            dp[0] = dp[1] = 1

        for i in range(2, n+1):
            if int(s[i-1]) > 0:
                dp[i] = dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]

        return dp[-1]
        ## R2:
        n = len(s)
        dp = [0]*(n+1)

        if s[0] != "0":
            dp[0] = 1
            dp[1] = 1

        for i in range(2, n+1):
            if 0 < int(s[i-1]):
                dp[i] = dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]

        return dp[-1]

        ## R1:
        n = len(s)
        dp = [0  for _ in range(n+1)]

        if s[0] != 0:
            dp[0] = dp[1] = 1

        for i in range(2, n+1):

            if 0 < int(s[i-1:i]) < 10:
                dp[i] += dp[i-1]

            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]

        return dp[n]


###########
def numDecodings(self, s: str) -> int:
        if not s or s[0]=='0':
            return 0

        dp = [0 for x in range(len(s) + 1)]

        # base case initialization
        dp[0:2] = [1,1]

        for i in range(2, len(s) + 1):
            # One step jump
            if 0 < int(s[i-1:i]):    #(2)
                dp[i] = dp[i - 1]
            # Two step jump
            if 10 <= int(s[i-2:i]) <= 26: #(3)
                dp[i] += dp[i - 2]

        return dp[-1]
