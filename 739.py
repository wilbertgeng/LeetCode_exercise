"""739. Daily Temperatures"""

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        ## R2:
        res = [0 for _ in range(len(T))]
        stack = []

        for pos, tem in enumerate(T):
            while stack and T[stack[-1]] < tem:
                cur = stack.pop()
                res[cur] = pos - cur
            stack.append(pos)

        return res



        ## R1:
        ans = [0 for _ in range(len(T))]
        stack = []

        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                cur = stack.pop()
                ans[cur] = i - cur

            stack.append(i)

        return ans
