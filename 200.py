"""200. Number of Islands"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ##### Prctice:
        self.m = len(grid)
        self.n = len(grid[0])
        cnt = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == '1':
                    self.dfs(i, j, grid)
                    cnt += 1
        return cnt

    def dfs(self, i, j, grid):
        if i < 0 or i >= self.m or j < 0 or j >= self.n or grid[i][j] == "0":
            return
        grid[i][j] = '0'

        self.dfs(i-1, j, grid)
        self.dfs(i+1, j, grid)
        self.dfs(i, j-1, grid)
        self.dfs(i, j+1, grid)



        ## R2:
        def dfs(i, j, grid):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == "0":
                return

            grid[i][j] = "0"

            dfs(i-1, j, grid)
            dfs(i+1, j, grid)
            dfs(i, j+1, grid)
            dfs(i, j-1, grid)

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    dfs(i, j, grid)
                    cnt += 1

        return cnt

        #### R1:
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i-1, j)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j-1)
        self.dfs(grid, i, j+1)
