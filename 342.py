"""342. Power of Four"""

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num != 0 and num&(num-1) == 0 and num&(0xAAAAAAAA) == 0
        ## another way
        return num > 0 and num & (num-1) == 0 and 0b1010101010101010101010101010101 & num == num
