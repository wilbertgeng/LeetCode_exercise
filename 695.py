"""695. Max Area of Island"""

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ### Practice:
        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            l = dfs(i-1, j)
            r = dfs(i+1, j)
            u = dfs(i, j-1)
            d = dfs(i, j+1)
            return l + r + u + d + 1  # be careful +1

        m = len(grid)
        n = len(grid[0])

        area_max = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    area_max = max(area_max, area)
        return area_max





        #######
        # dfs needs to be defined before use
        def dfs(i, j, grid):
            # exit conditions, set boundaries
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == 0:
                return 0
            grid[i][j] = 0

            up = dfs(i-1, j, grid)
            down = dfs(i+1, j, grid)
            left = dfs(i, j-1, grid)
            right = dfs(i, j+1, grid)

            return up + down + left + right + 1
        ## find max area
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                area = max(area, dfs(i, j, grid))
        return area
