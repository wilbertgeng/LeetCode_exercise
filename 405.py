"""405. Convert a Number to Hexadecimal"""

class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        ##############
        d = {10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
        if num == 0:
            return '0'
        if num < 0:
            num = num + 2**32
        res = ''

        while num:
            res = str(d[num%16] if num%16>9 else num%16) + res
            num /=16
        return res



        ##############
        d = {10:"a", 11:"b", 12:"c", 13:"d", 14:"e", 15:"f"}

        if num == 0:
            return "0"

        if num < 0:
            num = num + 2**32 ### flip the negative number to positive or ALT way: num &= 0xFFFFFFFF
        res = ''
    
        while n:
            res = str(d[n%16] if n%16>9 else n%16) + res
            n /= 16

        return res
