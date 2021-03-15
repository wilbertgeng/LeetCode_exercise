"""Next Greater Element II"""

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ## R2:
        stack = []
        res = [-1 for _ in range(len(nums))]

        for i in range(len(nums))*2:
            while stack and nums[stack[-1]] < nums[i]:
                cur = stack.pop()
                res[cur] = nums[i]

            stack.append(i)

        return res


        ## R1:
        stack = []

        res = [-1]*len(nums)

        for i in range(len(nums))*2:
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)

        return res
