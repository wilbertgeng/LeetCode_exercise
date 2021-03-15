"""566. Reshape the Matrix"""

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        m = len(nums[0])
        if m*n != r*c:
            return nums

        res = [[]]
        for i in range(n):
            for j in range(m):
                if len(res[-1]) < c:
                    res[-1].append(nums[i][j])

                else:
                    res.append([nums[i][j]])

        return res
        
