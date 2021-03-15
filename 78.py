"""78. Subsets"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ### Practice:
        self.res = []
        self.dfs(nums, [])
        return self.res

    def dfs(self, nums, path):
        self.res.append(path)

        for i in range(len(nums)):
            self.dfs(nums[i+1:], path + [nums[i]])


        # R3:
        res = []
        if not nums:
            return res

        def dfs(nums, path, res):

            res.append(path)
            for i in range(len(nums)):
                dfs(nums[i+1:], path + [nums[i]], res)

            return
        dfs(nums, [], res)
        return res

        # R2:
        res = []
        if not nums:
            return res

        def dfs(nums, cache, res):
            res.append(cache)

            for i in range(len(nums)):
                dfs(nums[i+1:], cache+[nums[i]], res)

            return

        dfs(nums, [], res)
        return res

        # R1:
        #solution 3 iteratively
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
        return result

        # [i+1:] from position i+1 to the end
        # [:i] from beginning to 4

    #solution1 DFS: runtime:81% mem:70%
    def Subsets1(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res
    def dfs(self, nums, path, res):
        res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], path + [nums[i]], res)

    #solution2: Bit Manipulation
    def Subset2(self, nums):
        res = []
        nums.sort()
        for i in xrange(1<<len(nums)):
            tmp = []
            for j in xrange(len(nums)):
                if i & 1 << j:  # if i >> j & 1:
                    tmp.append(nums[j])
            res.append(tmp)
        return res
