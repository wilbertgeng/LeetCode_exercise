"""190. Reverse Bits"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):

        res = 0
        for i in range(32):
            res = (res<<1)+(n&1) # don't forget brackets
            n = n >>1

        return res
