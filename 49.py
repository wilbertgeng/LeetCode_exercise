"""Group Anagrams"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for w in sorted(strs):     #no sorted is fine
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]

        return d.values()
