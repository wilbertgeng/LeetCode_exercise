"""168. Excel Sheet Column Title"""

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        # Practice:
        capitals = [chr(x) for x in range(ord("A"), ord("Z")+1)]
        res = ''
        while n != 0:
            res = str(capitals[(n-1)%26]) + res
            n = (n-1)/26
        return res


        ######
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        ## chr((num-1)%26+ord('A'))
        res = ''
        while num > 0:
            res = capitals[(num-1)%26] + res ## use (num-1)
            num = (num-1)/26

        return res
