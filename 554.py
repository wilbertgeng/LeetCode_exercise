"""554. Brick Wall"""

class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        h = {}
        length = 0
        for brick in wall:
            length = 0
            for n in brick:
                length += n
                h[length] = h.get(length, 0) + 1
            h[length] = 0

        length_most = max(list(h.values()))

        return len(wall) - length_most
