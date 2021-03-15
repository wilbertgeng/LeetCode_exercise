"""51. N-Queens"""

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ## Practice:
        res = []
        nums = [-1]*n
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        if index == len(nums): #触发结束条件：index(row) 超过 path(4) 的最后一行
            res.append(path)
            return
        for i in range(len(nums)):
            nums[index] = i
            if self.valid(nums, index): #排除不合法选择
                tmp = "."*len(nums)
                self.dfs(nums, index+1, path + [str(tmp[:i]+'Q'+tmp[i+1:])], res)

    def valid(self, nums, index):
        for i in range(index):
            #检查左上方是否有皇后互相冲突 or 检查列是否有皇后互相冲突
            if abs(nums[index]-nums[i])==index-i or nums[index]==nums[i]:
                return False
        return True

        ##

        res = []
        self.dfs([-1]*n, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        if index == len(nums):
            res.append(path)
            return

        for i in range(len(nums)):
            nums[index] = i
            if self.valid(nums, index):
                tmp = "."*len(nums)
                self.dfs(nums, index+1, path + [str(tmp[:i]+"Q"+tmp[i+1:])], res)

    def valid(self, nums, n):
        for i in range(n):
            if abs(nums[i]-nums[n]) == n - i or nums[i] == nums[n]:
                return False

        return True
