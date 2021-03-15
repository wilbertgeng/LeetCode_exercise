"""1239. Maximum Length of a Concatenated String with Unique Characters"""

class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        """ 1.use set to remove repeated character in each String
        2. use & | for set() """
        d = [set()] ## !! make sure there is an empty set inside so min val can be returned is 0
        for w in arr:
            if len(set(w)) != len(w):
                continue
            w = set(w)
            d.append(w)
            for l in d:
                if w&l:
                    continue
                d.append(w|l)

        return max(len(a) for a in d)
