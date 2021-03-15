"""46. Permutations"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """1、路径：也就是已经做出的选择。
        2、选择列表：也就是你当前可以做的选择。
        3、结束条件：也就是到达决策树底层，无法再做选择的条件。"""
        ## Template:
        result = []
        def backtrack(路径, 选择列表):
            if 满足结束条件:
                result.add(路径)
                return

        for 选择 in 选择列表:
            # 做选择
            将该选择从选择列表移除
            路径.add(选择)
            backtrack(路径, 选择列表)
            # 撤销选择
            路径.remove(选择)
            将该选择再加入选择列表
        #### Practice:
        self.res = []
        self.dfs(nums, [])
        return self.res

    def dfs(self, nums, path):
        if not nums:
            self.res.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path + [nums[i]])

        # R2:
        res = []
        self.dfs_backtrack(nums, [], res) #记录「路径」
        return res

    def dfs_backtrack(self, nums, path, res):
        if not nums: # 触发结束条件
            res.append(path)
            return

        for i in range(len(nums)): # 进入下一层决策树
            # path + [nums[i]] don't forget []
            self.dfs_backtrack(nums[:i] + nums[i+1:], path + [nums[i]], res)

        # R1:
        res = []
        path = []

        self.dfs(nums, path, res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)
