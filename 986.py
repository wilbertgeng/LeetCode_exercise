"""986. Interval List Intersections"""

class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        p1 = 0
        p2 = 0
        res = []
        while p1 < len(A) and p2 < len(B): # and
            a1, a2 = A[p1][0], A[p1][1]
            b1, b2 = B[p2][0], B[p2][1]
            if a1 <= b2 and b1 <= a2: # =
                res.append([max(a1, b1), min(a2, b2)])
            if b2 < a2:
                p2 += 1
            else:
                p1 += 1

        return res
