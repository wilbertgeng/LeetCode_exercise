"""303. Range Sum Query - Immutable"""

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sums = nums
        for i in range(1, len(nums)):
            self.sums[i] += nums[i-1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j] - self.sums[i-1] if i>0 else self.sums[j]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
