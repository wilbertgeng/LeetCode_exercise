"""3Sum
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #############
        






        #####
        res = []
        nums.sort()
        lastnum = float('inf')
        h = {}
        for i, num in enumerate(nums):
            ele = self.twoSum(num, nums[i+1:], -num)
            ele_t = tuple(ele)
            if ele_t not in h:
                h[ele_t] = 1
                res += ele
            else:
                continue

        return res

    def twoSum(self, num, nums, target):
        res = []
        l = 0
        r = len(nums) - 1
        while l < r:
            sum = nums[l] + nums[r]
            left = nums[l]
            right = nums[r]
            if sum == target:
                res.append([num, left, right])
                while l < r and nums[l]==left:
                    l += 1
                while l < r and nums[r]==right:
                    r -= 1
            elif sum < target:
                while l < r and nums[l]==left:
                    l += 1
            elif sum > target:
                while l < r and nums[r]==right:
                    r -= 1

        return res





        ################### wrong
        nums.sort()
        res = []
        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r :
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l< r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1

        return res
