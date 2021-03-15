"""378. Kth Smallest Element in a Sorted Matrix"""

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        ## heap
        res = 0
        ele = []

        for l in matrix:
            for e in l:
                heappush(ele, e)

        for i in range(k):
            res = heappop(ele)

        return res

        ##
        res = []
        for i in matrix:
            res += i

        return sorted(res)[k-1]
