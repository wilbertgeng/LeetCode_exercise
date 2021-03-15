"""260. Single Number III"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ### Practice:
        ab = nums[0]
        for i in range(1, len(nums)):
            ab = ab^nums[i]
        x = ab&~(ab-1)
        num1 = 0
        num2 = 0
        for num in nums:
            if num&x == 0:
                num1 = num1^num
            else:
                num2 = num2^num
        return [num1, num2]
        # find a, b
        ab = 0
        for num in nums:
            ab = ab ^ num

        x = ab&~(ab-1)
        num1 = 0
        num2 = 0

        for num in nums:
            if num & x == 0:
                num1 = num1^num
            else:
                num2 = num2 ^ num

        return [num1, num2]
