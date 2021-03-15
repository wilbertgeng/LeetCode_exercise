"""438. Find All Anagrams in a String"""

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        ########
        need = {}
        window = {}
        for char in p:
            need[char] = need.get(char, 0) + 1
        left = 0
        right = 0
        res = []
        valid = 0
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

            while right - left == len(p):
                d = s[left]
                if valid == len(need):
                    res.append(left)
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
                left += 1
        return res




        #########
        n_s = len(s)
        n_p = len(p)
        res = []
        map = {}
        for i in p:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1

        count = len(p)

        l, r = 0, 0
        while r < n_s:
            if s[r] in map:
                map[s[r]] -= 1

                if map[s[r]] >= 0:  # if got more of same char we need, it's useless
                    count -= 1

            if count == 0:
                res.append(l)

            if r == l + n_p - 1: # wait till {{left}} have exact {{lenP}} distance to {{right}}
                if s[l] in map:
                    map[s[l]] += 1
                     # if actual good stuff left, then desireCount += 1
                    if map[s[l]] >= 1:
                        count += 1
                l += 1

            r += 1

        return res
