"""179. Largest Number"""

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        self.quicksort(nums, 0, len(nums)-1)
        if sum(nums) == 0:
            return "0"
        res = ""
        for n in nums:
            res += str(n)
        return res

    def quicksort(self, nums, l, r):
        if l < r:
            pos = self.partition(nums, l, r)
            self.quicksort(nums, l, pos-1) # becareful of the position here
            self.quicksort(nums, pos+1, r)
    def partition(self, nums, l, r):
        low = l
        while l < r:
            if self.compare(nums[l], nums[r]):
                nums[low], nums[l] = nums[l], nums[low]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]

        return low

    def compare(self, n1, n2):
        return str(n1)+str(n2) > str(n2)+str(n1)










#
