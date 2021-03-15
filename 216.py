"""216. Combination Sum III"""

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ### Practice:
        self.res = []
        if n > 45:
            return []
        self.dfs(1, [], n, k)
        return self.res

    def dfs(self, start, path, target, cnt):
        if target == 0 and cnt == 0:
            self.res.append(path)
            return
        if cnt == 0:
            return
        for num in range(start, 10):
            if num > target:
                break
            self.dfs(num + 1, path + [num], target - num, cnt - 1)







        ## R2:
        if n > 45 or n < 1:
            return []
        res = []
        nums = list(range(1, 10))
        def dfs(nums, remain, path, cnt, res):
            if cnt > k:
                return
            if cnt == k and remain == 0:
                res.append(path)

            for i in range(0, len(nums)):
                if nums[i] > remain:
                    break
                else:
                    dfs(nums[i+1:], remain-nums[i], path + [nums[i]], cnt+1, res)

        dfs(nums, n, [], 0, res)

        return res

        ## R1:
        if n > 45 or n < 1:
            return []
        res = []
        candidates = list(range(1, 10))
        def dfs(nums, remain, cache, cnt, res):
            if cnt > k:
                return
            if cnt == k and remain == 0:
                res.append(cache)
                return
            for i in range(0, len(nums)):
                if nums[i] > remain:
                    break

                else:
                    dfs(nums[i+1:], remain-nums[i], cache+[nums[i]], cnt+1, res)

        dfs(candidates, n, [], 0, res)

        return res
