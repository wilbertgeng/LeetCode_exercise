"""693. Binary Number with Alternating Bits"""

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #######
        a = n^(n>>1)
        return a&(a+1) == 0


        #######
        a = n^(n>>1)
        return a&(a+1) == 0
