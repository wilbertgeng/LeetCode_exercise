"""684. Redundant Connection"""

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # union find: 1. Union 2. Find
        """OOD"""
        self.parent = [x for x in range(len(edges)+1)]
        for x, y in edges:
            if self.union(x, y):
                return [x, y]
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        if self.find(x) == self.find(y):
            return True
        self.parent[self.find(x)] = self.find(y)
        """  Non OOD  """
        parent = [x for x in range(len(edges)+1)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            if find(x) == find(y):
                return True
            parent[find(x)] = find(y)
        for x, y in edges:
            if union(x, y):
                return [x, y]
















###
