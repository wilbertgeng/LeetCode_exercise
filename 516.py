"""516. Longest Palindromic Subsequence"""

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if s == s[::-1]:
            return n

        dp = [0 for _ in range(n)]
        dp[-1] = 1

        for i in range(n-2, -1, -1):
            newdp = dp[:]
            newdp[i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    newdp[j] = 2 + dp[j - 1]

                else:
                    newdp[j] = max(dp[j], newdp[j-1])

            dp = newdp

        return dp[n-1]
