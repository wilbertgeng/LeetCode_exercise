"""240. Search a 2D Matrix II"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ## R2:
        # search from bottom left corner
        if not matrix:
            return False 
        row = len(matrix)-1
        col = 0
        width = len(matrix[0])-1

        while row >= 0 and col <= width:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target: # use elif not if
                col += 1
            elif matrix[row][col] > target:
                row -= 1

        return False
