"""77. Combinations"""

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ###### Practice:
        if k > n:
            return []
        self.res = []
        self.dfs(1, n+1, k, []) ## !! n+1 not n
        return self.res

    def dfs(self, start, n, cnt, path):
        if cnt == 0:
            self.res.append(path)
            return
        for num in range(start, n):
            self.dfs(num+1, n, cnt - 1, path + [num])





        #########
        res = []
        nums = list(range(1, n+1))
        self.dfs(res, [], nums, 0, k)
        return res

    def dfs(self, res, path, nums, cnt, k):
        if cnt == k:
            res.append(path)
            return
        for i in range(len(nums)):
            self.dfs(res, path + [nums[i]], nums[i+1:], cnt+1, k)
        #########
        path = []
        res = []

        def dfs(start, cnt, path, res):
            if cnt == k:
                res.append(path)
                return
            for i in range(start, n+1):
                dfs(i+1, cnt+1, path+[i], res)

        dfs(1, 0, [], res)

        return res
