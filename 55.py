"""Jump Game"""

class Solution(object):

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ##########
        last_position = len(nums)-1

        for i in range(len(nums)-2, -1, -1):   #range(start, stop, step)
            if (i + nums[i]) >= last_position:
                last_position = i

        print(last_position)

        return last_position == 0

s = Solution()
n = [2,3,1,1,4]
s.canJump(n)
