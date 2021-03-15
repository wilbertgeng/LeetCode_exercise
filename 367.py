"""367. Valid Perfect Square"""

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        ##### Practice:
        l = 0
        r = num
        while l <= r:
            mid = l + (r-l)//2
            if num == mid**2:
                return True
            elif num < mid**2:
                r = mid - 1
            else:
                l = mid + 1
        return False



        #####
        gap_num = 1

        while num > 0:
            num -= gap_num
            gap_num += 2

        return num == 0

        ## Binary search: much faster
        left = 0
        right = num

        while left <= right:
            mid = left + (right-left)//2
            if  mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                right = mid -1
            else:
                left = mid +1
        return False
