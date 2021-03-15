"""10. Regular Expression Matching"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ## DP
        dp = [[False]*(len(s)+1) for _ in range(len(p)+1)]
        dp[0][0] = True
        
