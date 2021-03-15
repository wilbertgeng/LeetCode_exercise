"""332. Reconstruct Itinerary"""

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        ######## Practice
        parent = {}
        for k, v in tickets:
            if k not in parent:
                parent[k] = [v] ## !! careful value is list
            else:
                parent[k].append(v)
        for k in parent:
            parent[k].sort(reverse=True) ## because we wanna return smallest lexical order result

        res = []
        stack = ['JFK']
        while stack:
            ele = stack[-1]
            if ele in parent and len(parent[ele])>0:
                stack.append(parent[ele].pop())
            else:
                res.append(stack.pop())
        return res[::-1]







        #######
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,  #why comma

        route = []

        def dfs(dprt):
            while targets[dprt]:
                dfs(targets[dprt].pop())
            route.append(dprt)


        dfs("JFK")

        return route[::-1]
