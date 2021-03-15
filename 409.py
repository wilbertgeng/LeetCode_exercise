"""409. Longest Palindrome"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        d = {}
        for l in s:
            d[l] = d.get(l, 0) + 1

        res = 0
        for l in d:
            res += d[l]/2*2

        return res if res == n else res+1
