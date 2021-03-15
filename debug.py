class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        total_sum = sum(nums)

        if (total_sum+S)%2==1 or S > total_sum:
            return 0

        target = (S+ total_sum)/2
        dp = [([1]+[0]*target)for _ in range(len(nums))]



        for j in range(target+1):
            if nums[0] == j:
                dp[0][j] = 1
        for i in range(1,len(nums)):
            for j in range(1, target+1):
                if nums[i] <= j:
                    dp[i][j] = dp[i-1][j-nums[i]] + dp[i-1][j]
                else:
                    dp[i][j] =  dp[i-1][j]

        return dp[-1][target]

s = Solution()
s.findTargetSumWays([0, 0, 0, 0, 0, 0, 0, 0, 1], 1)
print(dp[-1[-1]])
