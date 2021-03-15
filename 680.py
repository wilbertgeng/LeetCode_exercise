"""680. Valid Palindrome II"""

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # R2:
        s = list(s)

        i = 0
        j = len(s)-1

        while i <= j and s[i] == s[j]:
        
            i += 1
            j -= 1
        if i > j:
            return True
        left = s[i:j] ## skip s[j]
        right = s[i+1:j+1] ## skip s[i]
        return left == left[::-1] or right == right[::-1]
       
        # R1:
        s = list(s)

        i = 0
        j = len(s)-1

        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                left = s[i:j] ## skip s[j]
                right = s[i+1:j+1] ## skip s[i]
                return left == left[::-1] or right == right[::-1]
        return True
