"""88. Merge Sorted Array"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
    ####    ##### Merge Sort
        nums1[m:] = nums2
        self.mergeSort(nums1)

    def mergeSort(self, nums):
        if len(nums) > 1:
            l = 0
            r = len(nums)
            mid  = l + (r - l)//2
            L = nums[:mid]
            R = nums[mid:]
            self.mergeSort(L)
            self.mergeSort(R)
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



    ##########    ## Simple, fast way:
        nums1[m:] = nums2[:n]
        nums1.sort()

    ##########    ## Two pointers:
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m-1+n] = nums1[m-1]
                m -= 1
            elif nums1[m-1] <= nums2[n-1]:
                nums1[m-1+n] = nums2[n-1]
                n -= 1

        if n > 0:
            nums1[:n] = nums2[:n]
