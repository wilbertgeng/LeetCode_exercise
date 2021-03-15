"""452. Minimum Number of Arrows to Burst Balloons (Medium)"""

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key = lambda x: x[1])
        count = len(points)
        end = float('-inf')

        for s, e in points:
            if s > end:
                end = e
            else:
                count -= 1

        return count
                
