"""1122. Relative Sort Array"""

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        ####
        pos = {num:i for i, num in enumerate(arr2)}
        return sorted(arr1, key=lambda x: pos.get(x, 1000+x))

        ####
        return sorted(arr1, key = (arr2 + sorted(arr1)).index)
