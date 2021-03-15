"""217. Contains Duplicate"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #############
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                return True
        return False


        ###################
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        for num in nums:
            if d[num] >= 2:
                return True

        return False
