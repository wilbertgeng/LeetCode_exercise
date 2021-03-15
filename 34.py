"""34. Find First and Last Position of Element in Sorted Array"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ################
    

        ##############
        first = self.findFirstIndex(nums, target)
        last = self.findLastIndex(nums, target)

        if first == len(nums) or nums[first] != target:
            return [-1, -1]
        else:
            return [first, last]


    def findFirstIndex(self, nums, target):
        l = 0
        r = len(nums) ### be careful

        while l < r:
            mid = l + (r - l)//2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] >= target:
                r = mid

        return l

    def findLastIndex(self, nums, target):
        l = 0
        r = len(nums)

        while l < r:
            mid = l + (r - l)//2
            if nums[mid] > target:
                r = mid
            elif nums[mid] <= target:
                l = mid + 1
        return l - 1


    ### use only 1 function

        first = self.findFirstIndex(nums, target)
        last = self.findFirstIndex(nums, target + 1) - 1

        if first == len(nums) or nums[first] != target:
            return [-1, -1]
        else:
            return [first, last]


    def findFirstIndex(self, nums, target):
        l = 0
        r = len(nums) ### be careful

        while l < r:
            mid = l + (r - l)//2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] >= target:
                r = mid

        return l
