"""305. Number of Islands II"""

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        ""
        ## Practice:
        parent = {}
        count = 0
        res = []
        def find(n):
            if n != parent[n]:
                parent[n] = find(parent[n])
            return parent[n]

        def union(x, y):
            x = find(x)
            y = find(y)
            if x != y:
                parent[y] = x
                return 1
            return 0


        for i, j in positions:
            pos = (i, j)
            if pos not in parent:
                parent[pos] = pos
                count += 1
                for dir in (i-1, j),(i+1, j), (i, j-1), (i, j+1):
                    if dir in parent:
                        count -= union(pos, dir)
            res.append(count)
        return res

        ## Answer:
        parent = {}
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            x, y = find(x), find(y)
            if x == y:
                return 0
            #if rank[x] < rank[y]:
            #    x, y = y, x
            parent[y] = x
            #rank[x] += rank[x] == rank[y]
            return 1
        counts, count = [], 0
        for i, j in positions:
            if (i, j) not in parent:
                x = parent[x] = i, j
            #    rank[x] = 0
                count += 1
                for y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                    if y in parent:
                        count -= union(x, y)
                counts.append(count)
            else:
                counts.append(count)
        return counts









####
