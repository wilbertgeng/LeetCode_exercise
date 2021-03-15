"""646. Maximum Length of Pair Chain"""

class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """

        pairs.sort(key = lambda x: x[1])
        n = len(pairs)
        dp = [1]*n

        for i in range(1, n):
            for j in range(0, i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)
