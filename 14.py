"""14. Longest Common Prefix"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ## !! Just Prefix 
        if not strs:
            return ''
        shortest = min(strs, key = len)
        for i, l in enumerate(shortest):
            for item in strs:
                if item[i] != l:
                    return shortest[:i]

        return shortest
