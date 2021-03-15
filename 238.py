"""238. Product of Array Except Self"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ##### Practice:
        p = 1
        res = []
        for i in range(len(nums)):
            res.append(p)
            p *= nums[i]

        p = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= p
            p *= nums[i]
        return res



        ## R2:
        res = []
        p = 1
        for i in range(len(nums)):
            res.append(p)
            p = p*nums[i]

        p = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= p
            p *= nums[i]

        return res

        ## R1:
        output = []
        p = 1

        for i in range(len(nums)):
            output.append(p)
            p = p * nums[i]

        p = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] = output[i] * p
            p = p* nums[i]

        return output
