"""265. Paint House II"""
class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        dp = costs[0]
        n = len(costs[0])
        for i in range(1, len(costs)):
            pre = dp[:]
            for j in range(n):
                dp[j] = min(pre[:j]+pre[j+1:]) + costs[i][j]
        return min(dp)





"""Given a non-empty array of integers,
every element appears twice except for one.
 Find that single one.

Note:

Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = {}
        for num in nums:
            h[num] = h.get(num, 0) + 1
        for k, v in h.items():
            if v == 1:
                return k


"""solution 2"""
class Solution(object):
    def singleNumber(self, nums):

        return 2*(sum(set(nums)))-sum(nums)

"""solution3"""
class Solution(object):
    def singleNumber(self, nums):
        return reduce(lambda a, b: a^b , nums)
