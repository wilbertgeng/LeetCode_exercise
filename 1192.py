"""1192. Critical Connections in a Network"""

class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        ### Tarjan Algorithm
        def dfs(rank, curr, prev):
            low[curr] = rank
            for neighbor in edges[curr]:
                if neighbor == prev: ## can't go back to prev level
                    continue
                if not low[neighbor]:
                    dfs(rank + 1, neighbor, curr) ## go to next level
                low[curr] = min(low[curr], low[neighbor])
                if low[neighbor] >= rank + 1:
                    res.append([curr, neighbor])

        low = [0]*n
        edges = {i:[] for i in range(n)}
        for u, v in connections:
            edges[u].append(v)
            edges[v].append(u)
        res = []
        dfs(1, 0, -1)
        return res
