"""451. Sort Characters By Frequency"""

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        h = {}
        for letter in s:
            if letter not in h:
                h[letter] = 1
            else:
                h[letter] += 1

        freq = {}
        for k, v in h.iteritems():
            if v not in freq:
                freq[v] = [k]
            else:
                freq[v].append(k)

        for x in range(len(s), 0, -1):
            if x in freq:
                for a in freq[x]:
                    for _ in range(x):
                        res += str(a)

        return res
