"""526. Beautiful Arrangement"""

class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        """ 1. DFS Backtrack
        2. Save the pre-compute result with cache globally and reuse  """
        cache = {}
        def dfs(i, X):
            if i == 1:
                return 1
            key = (i, X)
            if key in cache:
                return cache[key]
            total = 0
            for j in range(len(X)):
                if X[j]%i == 0 or i%X[j] == 0:
                    total += dfs(i-1, X[:j]+X[j+1:])

            cache[key] = total
            return total
        return dfs(n, tuple(range(1, n+1)))
