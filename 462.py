"""462. Minimum Moves to Equal Array Elements II"""

class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ##### Practice
        nums.sort()
        moves = 0
        i = 0
        j = len(nums) - 1
        while i < j:
            moves += nums[j] - nums[i]
            i += 1
            j -= 1
        return moves

        ##########
        nums.sort()
        i = 0
        j = len(nums)-1
        moves = 0
        while i < j:
            moves += nums[j] - nums[i]
            i += 1
            j -= 1

        return moves

        ##### quick sort
        a = self.findKthsmallest(nums, len(nums)/2)
        # print(int(a))
        moves = 0
        for num in nums:
            moves += abs(num - a)

        return moves


    def findKthsmallest(self, nums, k):
        pos = self.partition(nums, len(nums)-1)
        if k == pos + 1:
            return nums[pos]
        if k < pos + 1:
            return self.findKthsmallest(nums[:pos], k)
        if k > pos + 1:
            return self.findKthsmallest(nums[pos+1:], k - pos -1)

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

s = Solution()
s.minMoves2([2,1])
print(a)
