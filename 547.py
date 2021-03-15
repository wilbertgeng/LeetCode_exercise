"""547. Number of Provinces (Friend Circles)"""

class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        #############
        seen = []
        m = len(isConnected)

        def dfs(i):
            for idx, num in enumerate(isConnected[i]):
                if num == 1 and idx not in seen:
                    seen.append(idx)
                    dfs(idx)
        cnt = 0
        for i in range(m):
            if i not in seen:
                dfs(i)
                cnt += 1
        return cnt



        ##############
        N = len(M)
        seen = set()

        def dfs(node):
            for ai, aj in enumerate(M[node]):
                ## aj exists(aj == 1) and ai not in seen!
                if aj and ai not in seen:
                    seen.add(ai)
                    dfs(ai)

        cnt = 0
        for i in range(N):
            if i not in seen:
                dfs(i)
                cnt += 1
        return cnt
