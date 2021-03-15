"""685. Redundant Connection II"""

class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        """There are 3 cases: 1. Graph has a circle
        2.1. vertex has two parents no circle
        2.2. vertex has two cirxles with circle
        Soltution:
        1: delete the last edge
        2.1: delete either one of the two edges
        2.2: delete the edge in the circle"""
        def find(u):
            if p[u] != u:
                p[u] = find(p[u])
            return p[u]
        def detect_circle(edge): # check if you can go from u to v as a circle
            u, v = edge
            while u != v and u in parents:
                u = parents[u]
            return u == v

        candidates = [] # store two edges from the vertex where it has two parents
        parents = {}
        for u, v in edges:
            if v not in parents:
                parents[v] = u
            else:
                candidates.append((parents[v], v))
                candidates.append((u,v))

        if candidates: # 2.1 2.2 when vertex has two parents
            return candidates[0] if detect_circle(candidates[0]) else candidates[1]
        else: # 1 perform a normal union find, same as 684.py 
            p = [x for x in range(len(edges)+1)]
            for u, v in edges:
                if find(u) == find(v):
                    return [u, v]
                else:
                    p[find(v)] = find(u)



















#########
