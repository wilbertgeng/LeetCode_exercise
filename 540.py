"""540. Single Element in a Sorted Array"""

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #################


        #################
        l = 0
        r = len(nums) - 1 # special case because m+1 is used below

        while l < r:
            m = l + (r - l)//2

            if m%2 == 0:
                if nums[m] == nums[m + 1]:
                    l = m + 1
                else:
                    r = m

            if m%2 == 1:
                if nums[m] == nums[m + 1]:
                    r = m
                else:
                    l = m + 1

        return nums[l]
