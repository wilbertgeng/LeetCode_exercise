"""1091. Shortest Path in Binary Matrix"""

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)

        def is_clear(cell):
            return grid[cell[0]][cell[1]] == 0

        def get_neighbours(cell):
            (i, j) = cell
            h = set()
            for a in (-1, 0, 1):
                for b in (-1, 0, 1):
                    if a != 0 or b != 0:
                        if 0 <= cell[0] + a < N and 0 <= cell[1] + b < N and is_clear((cell[0] + a, cell[1] + b)):
                            h.add((cell[0] + a, cell[1] + b)) #don't use append
            return h

        start = (0, 0)
        goal = (N - 1, N - 1)
        visited = set()

        queue = deque()
        if is_clear(start):
            queue.append(start)

        path_len = {start: 1}

        while queue:
            cell = queue.popleft() ## has to be popleft
            if cell in visited:
                continue ## return to beginning of loop
            if cell == goal:
                return path_len[cell]
        # if cell not in visited:
            visited.add(cell)
            for neighbor in get_neighbours(cell):
                if neighbor not in path_len:
                    path_len[neighbor] = path_len[cell] + 1
                queue.append(neighbor)

        return -1
