"""496. Next Greater Element I"""

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = {}
        stack = []
        ans = []
        for x in nums2:
            while stack and stack[-1] < x:
                d[stack.pop()] = x

            stack.append(x)

        for i in nums1:
            ans.append(d.get(i, -1))

        return ans
