"""219. Contains Duplicate II"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        d= {}

        for i, v in enumerate(nums):
            if v in d and i - d[v] <= k:
                return True

            d[v] = i

        return False
