"""213. House Robber II"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## Practice:

        def rob(nums):
            now = 0
            prev = 0
            for num in nums:
                now, prev = max(now, prev + num), now
            return now
        if len(nums) == 1:
            return nums[0]
        if not nums:
            return 0
        return max(rob(nums[:-1]), rob(nums[1:]))

        
        ## R2:
        if len(nums) <= 3:
            return max(nums)
        def rob_cycle(nums):
            last = 0
            now = 0
            for i in nums:
                last, now = now, max(now, last + i)

            return now

        return max(rob_cycle(nums[1:]), rob_cycle(nums[:-1]))
        ## R1:
