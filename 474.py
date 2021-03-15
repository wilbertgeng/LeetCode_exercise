"""474. Ones and Zeroes"""

class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        ## Practice again:
        nums = []
        for s in strs:
            zero = 0
            one = 0
            num = []
            for l in s:
                if l =="0":
                    zero += 1
                elif l == "1":
                    one += 1
            num.append(zero)
            num.append(one)
            nums.append(num)

        dp = [[0]*(m+1) for _ in range(n+1)]
        for zero, one in nums:
            for i in range(n, -1, -1):
                for j in range(m, -1, -1):
                    if i >= one and j >= zero:
                        dp[i][j] = max(1+dp[i-one][j-zero], dp[i][j])
        return dp[-1][-1]

        ## Practice:
        count = []
        for s in strs:
            ones = 0
            zeros = 0
            a = []
            for l in s:
                if l == "1":
                    ones += 1
                elif l == "0":
                    zeros += 1

            a.append(ones)
            a.append(zeros)
            count.append(a)

        dp = [[0]*(n+1) for _ in range(m+1)]
        for z, o in count:
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    if i >= o and j >= z:
                        dp[i][j] = max(1+dp[i-o][j-z], dp[i][j])

        return dp[m][n]
        ## my own way: bottom up style dp
        list = []

        for s in strs:
            zero = 0
            one = 0
            a = []
            for i in s:
                if i == "0":
                    zero += 1
                elif i == "1":
                    one += 1
            a.append(zero)
            a.append(one)
            list.append(a)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for k in range(len(strs)):
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    if i >= list[k][0] and j >= list[k][1]:
                        dp[i][j] = max(dp[i][j], dp[i-list[k][0]][j-list[k][1]]+1)
        return dp[-1][-1]
        ## A simplified version: backward iteration
        dp = [[0] * (n+1) for _ in range(m+1)]

        def count(s):
            return sum(1 for c in s if c == '0'), sum(1 for c in s if c == '1')

        for z, o in [count(s) for s in strs]:
            for x in range(m, -1, -1):
                for y in range(n, -1, -1):
                    if x >= z and y >= o:
                        dp[x][y] = max(1 + dp[x-z][y-o], dp[x][y])

        return dp[m][n]
        ##
        prev, curr = [[0]*(n+1) for _ in range(m+1)], [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, len(strs)+1):
            zeroes, ones = strs[i-1].count('0'), strs[i-1].count('1')
            for j in range(m+1):
                for k in range(n+1):
                    curr[j][k] = 0
                    if j >= zeroes and k >= ones:
                        curr[j][k] = max(prev[j][k], 1+prev[j-zeroes][k-ones])
                    else:
                        curr[j][k] = prev[j][k]
            prev, curr = curr, prev
        return prev[m][n]
