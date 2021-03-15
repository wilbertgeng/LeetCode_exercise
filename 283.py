."""283. Move Zeroes"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pt0 = 0
        pt1 = 0

        while pt1 < len(nums):

            if nums[pt0] == 0 and nums[pt1] != 0:
                nums[pt0], nums[pt1] = nums[pt1], nums[pt0]
                pt0 += 1
            if nums[pt0] != 0:
                pt0 += 1
            pt1 += 1

        ## solution 2:

        count=nums.count(0)
        nums[:]=[i for i in nums if i != 0]
        nums+=[0]*count
