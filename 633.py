"""633. Sum of Square Numbers"""

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i = 0
        j = int(c**0.5)

        while i <= j:
            if i**2 + j**2 == c:
                return True
            elif i**2 + j**2 < c:
                i += 1
            else:
                j -= 1

        return False
