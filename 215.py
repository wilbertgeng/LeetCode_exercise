"""215. Kth Largest Element in an Array"""

class Solution(object):
    """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ### review practice
    def findKthLargest(self, nums, k):
        return self.findKthsmallest(nums, len(nums) - k + 1)

    def findKthsmallest(self, nums, k):
        pos = self.partition(nums, len(nums) - 1)
        if k == pos + 1:
            return nums[pos]
        elif k > pos + 1:
            return self.findKthsmallest(nums[pos + 1:], k - pos - 1)
        elif k < pos + 1:
            return self.findKthsmallest(nums[:pos], k)

    def partition(self, nums, pivot):
        l = 0
        low = l
        while l < pivot:
            if nums[l] < nums[pivot]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[pivot] = nums[pivot], nums[low]
        return low



        ## O(n) time
    def findKthLargest(self, nums, k):
        ### R2 Quick selection:
        return self.findKthsmallest(nums, len(nums) - k + 1)

    def findKthsmallest(self, nums, k):
        pos = self.partition(nums, 0, len(nums) - 1)
        if k > pos +1:
            return self.findKthsmallest(nums[pos+1:], k - pos -1)
        elif k < pos + 1:
            return self.findKthsmallest(nums[:pos], k) ## find kth
        else:
            return nums[pos]

    def partition(self, nums, l, r):
        low = l
        while l < r:
            if nums[l] < nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low


    # O(nlogn) time
    def findKthLargest1(self, nums, k):
        return sorted(nums, reverse=True)[k-1]
# O(nk) time, bubble sort idea, TLE
    def findKthLargest2(self, nums, k):
        for i in range(k):
            for j in range(len(nums) - i - 1):
                if nums[j] > num[j +1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return nums[len(nums)-k]

# O(nk) time, selection sort idea:
        # similar as buble sort

# O(k+(n-k)lgk) time, min-heap:
    def findKthLargest4(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        for _ in range(len(nums) - k):
            heapq.heappop(heap)

        return heapq.heappop(heap)
