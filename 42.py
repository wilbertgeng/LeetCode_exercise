"""42. Trapping Rain Water"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        l = 0
        r = len(height)-1
        l_max = 0
        r_max = 0

        while l <= r:
            if l_max < r_max:
                if height[l] < l_max:
                    res += (l_max - height[l])
                l_max = max(l_max, height[l])
                l += 1

            else:
                if height[r] < r_max:
                    res += (r_max - height[r])
                r_max = max(r_max, height[r])
                r -= 1

        return res
