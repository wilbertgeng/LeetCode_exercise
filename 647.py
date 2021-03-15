"""647. Palindromic Substrings"""

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ## R2:
        n = len(s)
        ans = 0
        for i in range(2*n-1):
            left = i/2
            right = left + i%2
            while left >= 0 and right <= n-1 and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1

        return ans






        ## R1:
        N = len(s)
        ans = 0

        for i in range(2*N-1):
            left = i/2
            right = left + i%2
            while left >= 0 and right <= N and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1

        return ans
