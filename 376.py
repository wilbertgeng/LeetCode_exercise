"""376. Wiggle Subsequence"""

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## R2:
        if not nums:
            return 0
        up = 1
        down = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up = down + 1
            elif nums[i] < nums[i-1]:
                down = up + 1
        return max(up, down)


        ## R1:
        length = 1
        up = None # has to be none for initial condition

        if not nums:
            return 0

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1] and up != False:
                length += 1
                up = False
            if nums[i] > nums[i-1] and up != True:
                length += 1
                up = True

        return length
