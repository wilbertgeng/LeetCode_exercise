"""Container With Most Water
Medium
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2."""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        L, R, res, width = 0, len(height) - 1, 0, len(height) - 1

        for i in range(len(height) - 1, 0, -1):
            if height[L] >= height[R]:
                res = max(res, width*height[R])
                R -= 1
            else:
                res = max(res, width*height[L])
                L += 1
            width -= 1

        return res
