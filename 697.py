"""697. Degree of an Array"""

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # hashmap use dict, .values(), value type is list 
        d = {}

        for i, n in enumerate(nums):
            if n not in d:
                d[n] = [i]
            else:
                d[n].append(i)

        degreeMax = max([len(n) for n in d.values()]) # n is list!
        length = min([n[-1]-n[0] for n in d.values() if len(n) == degreeMax]) + 1

        return length
