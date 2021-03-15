"""Perfect Squares

Given a positive integer n,
find the least number of perfect square numbers
(for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        ## Practice:
        if n == 1:
            return 1
        dp = [i for i in range(n+1)]  ## !! range needs to match loop below
        for i in range(n+1):
            sqs = [j*j for j in range(1, int(sqrt(i))+1)]
            for sq in sqs:
                if sq <= i:
                    dp[i] = min(dp[i], dp[i-sq]+1)
        return dp[n]




        ### DP
        dp = [0]*(n+1)
        for i in range(1, n+1):
            n_min = float('inf')
            for j in range(1, int(sqrt(i))+1):
                n_min = min(n_min, dp[i-j*j]+1)
            dp[i] = n_min

        return dp[n]


        ## R4:
        if n< 2:
            return 0
        i = 1
        sqs = []
        while i*i <= n:
            sqs.append(i*i)
            i += 1

        cnt = 0
        to_check = [n]
        while to_check:
            cnt += 1
            temp = []
            for a in to_check:
                for b in sqs:
                    if b < a:
                        temp.append(a-b)
            to_check = temp

        return cnt

        ## R3:
        if n < 2:
            return n
        to_check = [n]
        i = 1
        list = []
        while i*i <= n:
            list.append(i*i)
            i += 1

        cnt = 0
        while to_check:
            cnt += 1
            tmp = []
            for x in list:
                for y in to_check:
                    if x == y:
                        return cnt
                    if x < y:
                        tmp.append(y-x)

            to_check = tmp

        return cnt


        ### R2:
        if n < 2:
            return n

        list = []
        i = 1
        while i*i < n:
            list.append(i*i)
            i += 1

        to_check = {n}
        cnt = 0
        while to_check:
            cnt += 1
            temp = set()
            for x in to_check:
                for y in list:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    temp.add(x-y)
                    to_check = temp
        return cnt


        ### R1:
        if n < 2:
            return n
        list = []
        i = 1
        while i*i <= n:
            list.append(i*i)
            i += 1
        toCheck = {n}
        cnt = 0
        while toCheck:
            cnt += 1
            temp = set()
            for x in toCheck:
                for y in list:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    temp.add(x-y) #don't use append

                    toCheck = temp
        return cnt














        if n < 2:
            return n
        lst = []
        i = 1
        while i * i <= n:
            lst.append( i * i )
            i += 1
        cnt = 0
        toCheck = {n}
        while toCheck:
            cnt += 1
            temp = set()
            for x in toCheck:
                for y in lst:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    temp.add(x-y)
            toCheck = temp

        return cnt













"""short solution"""

        if int(sqrt(n))**2 == n: return 1
        for j in range(int(sqrt(n)) + 1):
            if int(sqrt(n - j*j))**2 == n - j*j: return 2

        while n % 4 == 0:
            n >>= 2
        if n % 8 == 7: return 4
        return 3
#explaination:
    """First of all, there is a statement that any number can be represented as sum of 4 squares:
https://en.wikipedia.org/wiki/Lagrange's_four-square_theorem. So, answer always will be 4? No, when we talk about 4 squares, it means that some of them can be equal to zero. So, we have 4 options: either 1, 2, 3 or 4 squares and we need to choose one of these numbers.

How to check if number is full square? Just compare square of integer part of root and this number. Complexity of this part is O(1).
How to check if number is sum of 2 squares: n = i*i + j*j? iterate ovell all i < sqrt(n) and check that n - i*i is full square. Complexity of this part is O(sqrt(n)).
How to check that number is sum of 4 squares? In the same link for wikipedia:
by proving that a positive integer can be expressed as the sum of three squares if and only if it is not of the form 4^k(8m+7) for integers k and m. So, what we need to do is to check this condition and return true if it fulfilled. Complexity is O(log n)
Do we need to check anything else? No, because we have only one options left: 3 squares.
Complexity: time complexity is O(sqrt(n)) and space complexity is O(1)."""
