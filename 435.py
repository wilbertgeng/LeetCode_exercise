"""435. Non-overlapping Intervals"""

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        end = float('-inf')
        count = 0
        ## s, e in sorted(list) 
        for s, e in sorted(intervals, key = lambda x: x[1]):
            if s >= end:
                end = e
            else:
                count += 1


        return count
