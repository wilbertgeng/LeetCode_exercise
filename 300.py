class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # R2:
        ## DP O(n^2) too slow
        n = len(nums)
        dp = [1]*(n)
        if not nums:
            return 0

        for i in range(1, n):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
        # Binary search: O(nlogn)
        n = len(nums)
        tail = [0]*n
        size = 0
        for num in nums:
            i = 0
            j = size
            while i < j:
                m = (i+j)/2
                if tail[m] < num:
                    i = m + 1
                else:
                    j = m

            tail[i] = num
            size = max(size, i + 1)

        return size


        # R1:
        tails = [0]*len(nums)
        size = 0

        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j)//2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m

            tails[i] = x

            size = max(i+1, size)


        return size
