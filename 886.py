"""886. Possible Bipartition"""

class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        seen = {}

        self.graph = collections.defaultdict(list)
        for (u, v) in dislikes:                             # Create graph
            self.graph[u].append(v)
            self.graph[v].append(u)
            
        for i in range(1, N+1):
            if i not in seen:
                if self.check(seen, i, self.graph) == False:
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
