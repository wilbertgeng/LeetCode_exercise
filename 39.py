""" Combination Sum"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ## Practice:
        self.res = []
        candidates.sort()
        self.dfs(target, [], candidates)
        return self.res

    def dfs(self, target, path, candidates):
        if target == 0:
            self.res.append(path)
            return
        for item in candidates:
            if item > target:
                break
            if path and item > path[-1]:
                break
            else:
                self.dfs(target - item, path + [item], candidates)







        # R2:
        res = []
        candidates.sort()

        def dfs(remain, cache):
            if remain == 0:
                res.append(cache)
                return

            for item in candidates:
                if item > remain:
                    break
                # use > because 1. avoid repeat 2.here we try to fill remain with bigger number
                if cache and item > cache[-1]:
                    continue
                else:
                    dfs(remain-item, cache+[item])

        dfs(target, [])

        return res
###########










        # R1:
        result = []
        candidates = sorted(candidates)
        def dfs(remain, stack):
            if remain == 0:
                result.append(stack)
            # return

            for item in candidates:
                if item > remain: break
                if stack and item > stack[-1]:
                    continue
                else:
                    dfs(remain - item, stack + [item])

        dfs(target, [])
        return result
