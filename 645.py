"""645. Set Mismatch"""

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # R2:
        n = len(nums)
        sum_oringinal = (1+n)*n/2
        sum_NoDup = sum(set(nums))
        miss = sum_oringinal - sum_NoDup
        dup = sum(nums) - sum_NoDup

        return [miss, dup]



        # R1:
        n = len(nums)
        s = (1+n)*n//2
        t = sum(set(nums))
        miss = s - t
        duplicate = sum(nums) - t

        return [duplicate, miss]
