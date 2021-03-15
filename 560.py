"""560. Subarray Sum Equals K"""

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        sum = 0
        d = {}
        d[0] = 1
        for i in range(len(nums)):
            sum += nums[i]
            count += d.get(sum - k, 0)
            d[sum] = d.get(sum, 0) + 1

        return count
