"""628. Maximum Product of Three Numbers"""

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ##### Practice
        nums.sort()
        a = 1
        for i in range(len(nums)-1, len(nums)-4, -1):
            a *= nums[i]
        b = 1
        for i in range(2):
            b *= nums[i]
        return max(b*nums[-1], a)

        #####
        nums.sort()
        a = 1
        for i in range(len(nums)-1, len(nums)-4, -1):
            a = a* nums[i]

        b = 1
        for j in range(2):
            b = b* nums[j]

        return max(b*nums[-1], a)
