"""40. Combination Sum II"""

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ### Practice:
        candidates.sort()
        self.res = []
        self.dfs(target, [], candidates)
        return self.res
    def dfs(self, target, path, nums):

        if target == 0:
            self.res.append(path)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: #### !!!
                continue
            if nums[i] > target:
                break
            self.dfs(target - nums[i], path + [nums[i]], nums[i+1:])



        #########
        candidates.sort()
        result = []
        self.combine_sum_2(candidates, 0, [], result, target)
        return result

    def combine_sum_2(self, nums, start, path, result, target):
        # Base case: if the sum of the path satisfies the target, we will consider
        # it as a solution, and stop there
        if not target:
            result.append(path)
            return

        for i in xrange(start, len(nums)):
            # Very important here! We don't use `i > 0` because we always want
            # to count the first element in this recursive step even if it is the same
            # as one before. To avoid overcounting, we just ignore the duplicates
            # after the first element.
            if i > start and nums[i] == nums[i - 1]:
                continue

            # If the current element is bigger than the assigned target, there is
            # no need to keep searching, since all the numbers are positive
            if nums[i] > target:
                break

            # We change the start to `i + 1` because one element only could
            # be used once
            self.combine_sum_2(nums, i + 1, path + [nums[i]],
                               result, target - nums[i])







###########
