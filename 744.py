"""744. Find Smallest Letter Greater Than Target"""

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        ##############
        l = 0
        r = len(letters)
        while l <= r:
            mid = l + (r-l)/2
            if letters[mid]> target >= letters[mid-1]:
                return letters[mid]
            elif letters[mid] <= target:
                l = mid + 1
            elif letters[mid] > target:
                r = mid - 1

        return letters[0]
        ###############
        for letter in letters:
            if letter > target:
                return letter

        return letters[0]

        ## binary search
        l = 0
        r = len(letters) - 1

        while l <= r:
            m = l + (r - l)//2
            if letters[m] <= target:
                l = m + 1

            elif letters[m-1] <= target < letters[m]:
                return letters[m]

            else:
                r = m - 1

        return letters[0]
