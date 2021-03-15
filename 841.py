"""841. Keys and Rooms"""

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
         n = len(rooms)
        visited = [1]+[0]*(n-1)

        def dfs(key):
            if visited[key] == 1:
                return
            visited[key] = 1
            for k in rooms[key]:
                dfs(k)
        if rooms[0]:
            for key in rooms[0]:
                if visited[key] == 0:
                    dfs(key)

        return sum(visited) == n
