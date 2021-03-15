"""698. Partition to K Equal Sum Subsets"""

class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        ####
        total = sum(nums)
        if total%k != 0:
            return False
        target = total/k
        buckets = [target]*k
        nums.sort(reverse = True)


        def dfs(pos):
            if pos == len(nums):
                return True
            for i in range(k):
                if buckets[i] >= nums[pos]:
                    buckets[i] -= nums[pos]
                    if dfs(pos + 1):
                        return True
                    buckets[i] += nums[pos]
            return False

        return dfs(0)







##########
