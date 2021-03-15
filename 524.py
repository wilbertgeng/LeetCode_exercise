"""524. Longest Word in Dictionary through Deleting"""

class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        ## practice: even faster
        d.sort(key = lambda x: (-len(x), x))

        for w in d:
            n = 0
            for l in s:
                if l == w[n]:
                    n += 1
                    if n == len(w):
                        return w
        return ""
        ## 2 for loops

        d.sort(key = lambda x: (-len(x), x))
        for word in d:
            i = 0
            for letter in s:
                if i < len(word) and letter == word[i]:
                    i += 1
                if i == len(word):
                    return word

        return ''
