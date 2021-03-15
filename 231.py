"""231. Power of Two"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ######### Practice
        if n == 0:
            return False # Be careful

        a = n&(n-1)
        if a == 0:
            return True
        else:
            return False
        #########
         a = n&(n-1)

        if n == 0:
            return False

        if a == 0:
            return True
        else:
            return False
