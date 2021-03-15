"""326. Power of Three"""

class Solution(object):
    def isPowerOfThree(self, num):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 1162261467 % n == 0

        ### while loop:
        if n <= 0:
            return False

        while n%3 == 0:
            n /= 3 

        return n == 1
