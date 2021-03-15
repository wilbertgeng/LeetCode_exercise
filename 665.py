"""665. Non-decreasing Array"""

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                count += 1
                if i == 0: ##initial case
                    continue
        ## normal case check if nums[i+1] smaller than both nums[i] and nums[i-1]
                if nums[i-1] > nums[i+1]:
                    nums[i+1] = nums[i]

            if count > 1:
                return False

        return True 
