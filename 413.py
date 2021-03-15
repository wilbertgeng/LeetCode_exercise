"""413. Arithmetic Slices"""

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ### Practice:
        n = len(A)
        if n < 3:
            return 0
        dp = [0]*n
        for i in range(2, n):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp[i] = dp[i-1] + 1
        return sum(dp)


        ## R2:
        n = len(A)
        if n < 3:
            return 0

        dp = [0]*n
        for i in range(2, n):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp[i] = dp[i-1] + 1

        total = 0

        for i in range(n):
            total += dp[i]

        return total

        ## R1:
        if len(A) < 3:
            return 0

        dp = [0]*len(A)
        for i in range(2, len(A)):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                dp[i] = dp[i-1]+1

        total = 0

        for i in range(len(A)):
            total += dp[i]

        return total
