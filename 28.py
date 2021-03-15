"""28. Implement strStr()"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        ## Robin Karp
        BASE = 1000000

        m = len(needle)

        if not needle:
            return -1

        power = 1
        for i in range(m):
            power = (power * 31) % BASE

        targetCode = 0
        for i in range(m):
            targetCode = (targetCode * 31 + needle[i]) % BASE

        hashCode = 0
        for i in range(len(haystack)):
            hashCode = (hashCode * 31 + needle[i]) % BASE
            if i < m - 1:
                continue
            if i >= m:
                hashCode = hashCode - (haystack[i - m] * power) % BASE
                if hashCode < 0:
                    hashCode += BASE
            if hashCode == targetCode:
                if haystack[i - m + 1: i + 1] == needle:
                    return i - m + 1

        return -1






        ## O(n^2)
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
            else:
                return i

        return -1
