"""345. Reverse Vowels of a String"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        ## R2:
       
        ## R1:
        s = list(s)
        vows = set('aeiouAEIOU') ## use set
        l = 0
        r = len(s)-1

        while l < r:
            while l < r and s[l] not in vows:
                l += 1
            while l < r and s[r] not in vows:
                r -= 1

            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        return ''.join(s) ## return string 
