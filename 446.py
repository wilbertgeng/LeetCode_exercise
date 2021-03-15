"""446. Arithmetic Slices II - Subsequence"""

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp = [collections.defaultdict(int) for _ in range(len(A))]
        total = 0
        for i in range(len(A)):
            for j in range(i):
                k = A[i] - A[j]
                dp[i][k] += 1
                if k in dp[j]:
                    dp[i][k] += dp[j][k]
                    total += dp[j][k]
        return total



















######
