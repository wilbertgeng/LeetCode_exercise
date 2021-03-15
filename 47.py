"""47. Permutations II"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #### Practice:
        nums.sort()
        self.res = []
        self.dfs(nums, [])
        return self.res

    def dfs(self, nums, path):
        if not nums:
            self.res.append(path)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[:i]+nums[i+1:], path + [nums[i]]) ## !! + []



        #########
        res = []
        nums.sort()
        self.dfs(res, nums, [])
        return res

    def dfs(self, res, nums, path):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue # 排除不合法的选择
            else: # 进入下一层决策树
                self.dfs(res, nums[:i]+nums[i+1:], path+[nums[i]])

        ############
        n = len(nums)
        res = []
        nums.sort()

        def dfs_backtrack(nums, l):
            if l == n-1:
                # use list()
                res.append(list(nums))
                return

            for i in range(l, n):
                if i > l and nums[i] == nums[l]:
                    continue
                nums[i], nums[l] = nums[l], nums[i]
                dfs_backtrack(list(nums), l + 1)

        dfs_backtrack(nums, 0)
        return res
