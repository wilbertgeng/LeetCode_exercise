"""323. Number of Connected Components in an Undirected Graph"""
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        parent = {i:i for i in range(n)}
        count = n
        def find(n):
            if parent[n] != n:
                parent[n] = find(parent[n])
            return parent[n]

        def union(x, y):
            x = find(x)
            y = find(y)
            if x != y:
                parent[y] = x
                return 1
            return 0

        for i, j in edges:
            if parent[i] != parent[j]:
                count -= union(i, j)

        return count 
