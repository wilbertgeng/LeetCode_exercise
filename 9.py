"""9. Palindrome Number"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # reverse the number 
        if x < 0:
            return False

        p = x
        res = 0
        while p:
            res = res*10 + p%10
            p /= 10

        return res == x
