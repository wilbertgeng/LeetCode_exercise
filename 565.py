"""565. Array Nesting"""

class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #
        n = len(nums)
        seen = [0]*n
        res = 0
        # no need to restore seen, loops are isolated, no ele is repeated
        for i in range(n):
            cnt = 0
            while seen[i] == 0:
                seen[i] = 1
                cnt += 1
                i = nums[i]

            res = max(res, cnt)

        return res
