"""912. Sort an Array"""

class Solution(object):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
"""Quick Sort"""
    def sortArray(self, nums):
        self.quickSortHelp(nums, 0 , len(nums)-1)
        return nums
    def quickSortHelp(self, nums, start, end):
        if start < end:
            pos = self.partition(nums, start, end)
            self.quickSortHelp(nums, start, pos - 1)
            self.quickSortHelp(nums, pos + 1, end)
    def partition(self, nums, low, pivot):
        l = low
        while l < pivot:
            if nums[l] < nums[pivot]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[pivot] = nums[pivot], nums[low]
        return low

"""Merge Sort"""
    def sortArray(self, nums):
        if len(nums) > 1:
            l = 0
            r = len(nums) ## Be acreful no -1 think about if len(nums) = 2
            mid = l + (r - l)//2
            L = nums[:mid]
            R = nums[mid:]
            self.sortArray(L)
            self.sortArray(R)

            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    nums[k] = L[i]
                    i += 1
                else:
                    nums[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                nums[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                nums[k] = R[j]
                j += 1
                k += 1
        return nums

"""Bubble Sort"""
    def sortArray(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums















##########
