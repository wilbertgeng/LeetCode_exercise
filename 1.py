#Two sum
"""Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]."""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            if target - nums[i] not in d:
                d[nums[i]] = i
            else:
                return [i, d[target -nums[i]]]
        #### two pointers
        """ in this problem nums shouldn't be sorted two pointers solution below return
        elements not indices """
        nums.sort()
        res = []
        l = 0
        r = len(nums) - 1
        while l < r:
            sum = nums[l] + nums[r]
            left = nums[l]
            right = nums[r]
            if sum == target:
                res.append([left, right])
                while l < r and nums[l]==left:
                    l += 1
                while l < r and nums[r]==right:
                    r -= 1
                l += 1
                r -= 1
            elif sum < target:
                while l < h and nums[l]==left:
                    l += 1
            elif sum > target:
                while l < r and nums[r]==right:
                    r -= 1

        return res


        ## R2:
        d = {}
        for i, num in enumerate(nums):
            if target - num not in d:
                d[num] = i
            else:
                return [d[target- num], i]



        ## R1:
        if len(nums) <= 1:
            return False
        h = {}
        for i in range (len(nums)):
            if nums[i] in h:
                return [h[nums[i]],i]
            else:
                h[target-nums[i]] = i

#solution 2:
        h = {}
        for i, num in enumerate(nums):
            if num in h:
                return h[target - num], i
                h[num] = i
