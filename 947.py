"""947. Most Stones Removed with Same Row or Column"""

class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        ## DFS
        def dfs(i, j):
            visited.add((i, j))
            for y in row[i]:
                if (i, y) not in visited:
                    dfs(i, y)
            for x in col[j]:
                if (x, j) not in visited:
                    dfs(x, j)

        row = collections.defaultdict(list)
        col = collections.defaultdict(list)
        num_island = 0
        for i, j in stones:
            row[i].append(j)
            col[j].append(i)

        visited = set()
        for i, j in stones:
            if (i, j) not in visited:
                dfs(i, j)
                num_island += 1

        return len(stones) - num_island


        ## Union Find
        d = {}

        def find(n):
            if d[n] != n:
                d[n] = find(d[n])
            return d[n]

        def union(x, y):
            d.setdefault(x, x)
            d.setdefault(y, y)
            d[find(x)] = find(y)

        for i, j in stones:
            union(i, ~j)

        return len(stones) - len({find(x) for x in d})
