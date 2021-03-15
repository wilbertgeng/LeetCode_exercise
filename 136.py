"""Single Number


Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## bit manipulation
        a = nums[0]
        for i in range(1, len(nums)):
            a = a^nums[i]

        return a
        ## R1:
        h = []
        for ele in nums:
            if ele not in h:
                h.append(ele)
            else:
                h.remove(ele)

        return h.pop()
