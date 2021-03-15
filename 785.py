"""785. Is Graph Bipartite?"""

class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        ### adjacent vertices should have diff colors
        ## practice
        seen = {}
        for i in range(len(graph)):
            if i not in seen:
                if not self.check(i, seen, graph):
                    return False
                continue
        return True

    def check(self, i, seen, graph):
        q = [(i, 1)]
        while q:
            node, color = q.pop(0)
            if node in seen:
                if seen[node] != color:
                    return False
                continue
            seen[node] = color
            for pos in graph[node]:
                q.append((pos, -color))
        return True

        ## BFS:
        seen = {}
        for i in range(len(graph)):
            if i not in seen:
                if self.check(seen, i, graph) == False:
                    return False

        return True

    def check(self, seen, i, graph):
        q = [(i, 1)]
        while q:
            pos, color = q.pop(0)
            if pos in seen:
                if seen[pos] != color:
                    return False
                continue

            seen[pos] = color
            vertices = graph[pos]
            for v in vertices:
                q.append((v, -color))

        return True
