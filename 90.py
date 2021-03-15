"""90. Subsets II"""

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ## Practice:
        self.res = []
        nums.sort()
        self.dfs(nums, [])
        return self.res

    def dfs(self, nums, path):
        self.res.append(path)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[i+1:], path + [nums[i]])

        ## R2:
        res = []
        if not nums:
            return res

        nums.sort() # remember to sort!

        def dfs(nums, path, res):
            res.append(path)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                else:
                    dfs(nums[i+1:], path + [nums[i]], res)
            return

        dfs(nums, [], res)

        return res

        ## R1:
###################
# if sorted() is used
        res = []
        if not nums:
            return res
        nums.sort()
        def dfs(nums, cache, res):
            res.append(cache)

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                dfs(nums[i+1:], cache+[nums[i]], res)

            return

        dfs(nums, [], res)
        return res
