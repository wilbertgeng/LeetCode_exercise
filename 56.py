"""Merge Intervals"""

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        ###### Practice again
        res = []
        intervals.sort(key = lambda x: (x[0], x[1]))
        for intv in intervals:
            if res and intv[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], intv[1])
            else:
                res.append(intv)
        return res

        ################# prictice
        out = []
        intervals.sort(key = lambda x:x[0])
        for intv in intervals:
            if out and intv[0] <= out[-1][1]:
                out[-1][1] = max(intv[1], out[-1][1])
            else:
                out.append(intv)

        return out



        #################
        out = []

        for i in sorted(intervals, key=lambda i: i[0]):
            if out and i[0] <= out[-1][-1]:
                out[-1][-1] = max(i[-1], out[-1][-1])
            else:
                out.append(i)
            #The i, is a tuple (because of the comma), and you can += a tuple to a list.

        return out
