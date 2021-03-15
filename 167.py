"""167. Two Sum II - Input array is sorted"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        j = len(numbers)-1
        i = 0
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1] #returned answers (both index1 and index2) are not zero-based
            if numbers[i] + numbers[j] < target:
                i += 1
            if numbers[i] + numbers[j] > target:
                j -= 1

        return None
