"""1288. Remove Covered Intervals 删除被覆盖区间"""
class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        ##### Practice
        intervals.sort(key = lambda x: (x[0], -x[1]))
        res = []
        if not intervals:
            return 0

        res.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][1] > res[-1][1]:
                res.append(intervals[i])
        return len(res)


        ######
        intervals.sort(key = lambda x:(x[0], -x[1]))
        left = intervals[0][0]
        right = intervals[0][1]

        res = 0
        for i in range(1, len(intervals)):
            intv = intervals[i]
            if left <= intv[0] and right >= intv[1]:
                res += 1
            elif right >= intv[0] and right < intv[1]:
                right = intv[1]
            elif right < intv[0]:
                left = intv[0]
                right = intv[1]

        return len(intervals) - res
