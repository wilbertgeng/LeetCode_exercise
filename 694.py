"""694. Number of Distinct Islands"""

class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ####### Use string to record shape of island and store in hashset
        m = len(grid)
        n = len(grid[0])
        def dfs(i, j, area):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return "0"
            grid[i][j] = 0
            u = dfs(i-1, j,  area)
            l = dfs(i,  j-1,  area)
            d = dfs(i+1, j, area)
            r = dfs(i, j+1, area)

            area = u + d + l + r + "1"

            return area
        res = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = "0"
                    res.add(dfs(i, j, area))

        return len(res)
