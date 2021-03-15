"""504. Base 7"""

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        #########
        if num == 0:
            return "0"
        n = abs(num)
        res = ''
        while n:
            res = str(n%7) + res
            n = n/7

        return ('-'+res) if num < 0 else res
        ###########
        if num == 0:
            return '0'
        n = abs(num)
        res = ''
        while n:
            res = str(n%7) + res
            n = n/7

        return ('-' + res) if num < 0 else res
