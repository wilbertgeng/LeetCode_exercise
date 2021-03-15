"""Counting Bits"""

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        #######
        res = [0]
        for n in range(1, num+1):
            res.append(res[n>>1]+int(n&1))
        return res
        #######
        res = [0]
        for n in range(1, num+1):
            res.append(res[n>>1] + int(n&1))

        return res
