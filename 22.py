"""Generate Parentheses
Given n pairs of parentheses,
write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ######Practice:
        self.res = []
        self.dfs(n, n, '')

        return self.res

    def dfs(self, n, k, path):
        if k == 0 and n == 0:
                self.res.append(path)
                return
        if n < k:
            return
        if n > 0:
            self.dfs(n-1, k, path+ ')')
        if k > 0:
            self.dfs(n, k-1, path +'(')






        ########
        if n == 0:
            return []
        res = []
        self.backtrack(res, n, n, '')
        return res

    def backtrack(self, res, l, r, path):
        if l > r:
            return
        if l > 0:
            self.backtrack(res, l-1, r, path + '(')
        if r > 0:
            self.backtrack(res, l, r-1, path + ')')
        if l == 0 and r == 0:
            res.append(path)


        #################
        if n == 0:
            return []

        res = []
        self.helper(n, n, "", res)
        return res

    def helper(self, l, r, item, res ):
        if l > r:
            return

        if l > 0:

            self.helper(l-1, r, item + "(", res)
        if r > 0:

            self.helper(l, r-1, item + ")", res)
        if l == 0 and r == 0:
            res.append(item)

#short version solution:
def generateParenthesis(self, n):
    def generate(p, left, right, parens=[]):
        if left:         generate(p + '(', left-1, right)
        if right > left: generate(p + ')', left, right-1)
        if not right:    parens += p,
        return parens
    return generate('', n, n)
