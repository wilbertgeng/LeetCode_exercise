"""461. Hamming Distance"""

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        #### Practice:

        #####
        a = x^y
        cnt = 0

        while a:
            cnt += 1
            a = a&(a-1)

        return cnt
