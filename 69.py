"""69. Sqrt(x)"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        #####Practice

    
        ###############
        l = 0
        r = x

        while l <= r:
            mid = l + (r - l)//2
            if mid*mid <= x < (mid+1)*(mid+1):
                return mid
            elif mid*mid > x:
                r = mid - 1
            else:
                l = mid + 1

        ### short way

        r = x

        while r*r > x:
            r = (r + x/r)//2

        return r
