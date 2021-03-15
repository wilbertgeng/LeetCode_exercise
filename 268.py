"""268. Missing Number"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ##### Practice:
        n = len(nums)
        a = n*(n+1)/2
        b = sum(nums)
        return a-b
        ####
        nums.sort()
        full_nums = range(len(nums)+1) # l = range(n)

        for i in range(len(nums)):
            if nums[i]^full_nums[i] != 0:
                return full_nums[i]

        return full_nums[-1]
