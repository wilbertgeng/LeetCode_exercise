"""153. Find Minimum in Rotated Sorted Array"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #######################
        l = 0
        r = len(nums) - 1 # special case: equal get rid of last ele 
        num = nums[-1]

        while l < r:
            m = l + (r - l)/2
            if nums[m] > num:
                l = m + 1
            elif nums[m] < num:
                r = m

        return nums[l]

        #############
        l = 0
        r = len(nums) - 1
        last_value = nums[-1]

        while l < r:
            mid = l + (r - l)//2

            if nums[mid] > last_value:
                l = mid + 1

            elif nums[mid] < last_value:
                r = mid

        return nums[l]








#
