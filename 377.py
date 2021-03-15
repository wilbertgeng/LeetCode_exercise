"""377. Combination Sum IV"""

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ########## Practice:
        dp = [1] + [0]*target
        for i in range(target+1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]

        return dp[target]

        ##########
        n = len(nums)
        nums.sort()
        dp = [1]+[0]*target
        # recursion oder opposite to coin change 2
        for i in range(1, target+1):
            for num in nums:
                if i >= num:
                    dp[i] = dp[i]+ dp[i-num]

        return dp[-1]
