"""256. Paint House"""

class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        ## O(3*n)
        if not costs:
            return 0
        n = len(costs)
        dp = [[0,0,0] for _ in range(n)]
        dp[0] = costs[0]
        for i in range(1, n):
            dp[i][0] = min(dp[i-1][1:3]) + costs[i][0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][2])+ costs[i][1]
            dp[i][2] = min(dp[i-1][0:2])+ costs[i][2]
        return min(dp[n-1])

        ## O(1)
        if not costs:
            return 0
        dp = costs[0]
        for i in range(1, len(costs)):
            pre = dp
            dp[0] = min(pre[1:3]) + costs[i][0]
            dp[1] = min(pre[0], pre[2]) + costs[i][1]
            dp[2] = min(pre[0:2]) + costs[i][2]
        return min(dp)





















########
