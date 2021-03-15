"""287. Find the Duplicate Number"""

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # R3: fast
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                return num
        # R3: Fast
        n = len(nums)
        nums.sort()
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                return nums[i]


        # R2:
        ## binary search, even slower
        left, right = 1, len(nums)-1
        while left < right:
           mid = (right + left)/2
           left, right = [left, mid] if sum(i <= mid for i in nums) > mid else [mid+1, right]
        return right


        # 2 pointers
        slow = 0
        fast = 1
        nums.sort()
        while nums[slow] != nums[fast] and fast <= len(nums)-1:
            if nums[slow] != nums[fast]:
                slow += 1
                fast += 1
            else:
                slow += 1

        return nums[slow]
        # R1:
        fast = 1
        slow = 0
        nums.sort()
        while fast != slow and fast <= len(nums)-1:
            if nums[fast] != nums[slow]:
                fast += 1
                slow += 1
            else:
                slow += 1

        return nums[fast]
