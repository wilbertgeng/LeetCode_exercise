"""455. Assign Cookies"""

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        cookie = 0
        child = 0

        while cookie <= len(s)-1 and child <= len(g)-1:
            if s[cookie] >= g[child]:
                child += 1
            cookie += 1

        return child
