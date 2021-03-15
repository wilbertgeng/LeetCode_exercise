"""485. Max Consecutive Ones"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        cnt_max = 0
        cnt = 0
        while i < len(nums):
            if nums[i] == 1:
                cnt += 1
            else:
                cnt = 0
            i += 1

            cnt_max = max(cnt_max, cnt)


        return cnt_max
