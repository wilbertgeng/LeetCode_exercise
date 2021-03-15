"""476. Number Complement"""

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        ######
        
        ######
        i = 1
        # create 1111..
        while i <= num:
            i = i<<1

        return (i-1)^num
