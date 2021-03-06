"""Climbing Stairs
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ### Practice:
        dp = [0]*(n+1)
        dp[1] = 1
        if n > 1: ## !! don't forget this
            dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]





        ## Review:
        now = 1
        next = 1
        if n <= 2:
            return n
        else:
            for i in range(n):
                now, next = next, now + next
        return now
        # R2:
        step = 1
        next = 1
        if n <= 2:
            step = n
        else:
            for i in range(n):
                step, next = next, step + next

        return step



        # R1:
        a, b = 1 ,1
        if n <= 2:
            step = n
        else:
            for i in range(n):
                a, b = b, a + b
                step = a

        return step
