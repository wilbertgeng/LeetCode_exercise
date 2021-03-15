"""318. Maximum Product of Word Lengths"""

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        ####### Practice:
        d = {}
        for w in words:
            mask = 0
            for l in w:
                mask = mask | (1<<(ord(l)-ord('a')))
            d[mask] = max(d.get(mask, 0), len(w))
        res = 0
        for x in d:
            for y in d:
                if not x&y:
                    res = max(res, d[x]*d[y])
        return res
        
        ##########
        d = {}

        for w in words:
            mask = 0
            for l in w:
                mask = mask | (1<<(ord(l)-ord("a")))

            d[mask] = max(d.get(mask, 0), len(w))
        # two words don't share common letters
        res = max([d[x]*d[y] for x in d for y in d if not x&y] or [0])

        return res
