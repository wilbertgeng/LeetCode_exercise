"""594. Longest Harmonious Subsequence"""

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ###### Practice
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1

        res = 0
        for n in nums:
            if n+1 in d:
                res = max(res, d[n]+d[n+1])
        return res



        ############
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        ans = 0
        for num in nums:
            if num+1 in d:
                ans = max(ans, d[num]+d[num+1])

        return ans
