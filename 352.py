"""352. Data Stream as Disjoint Intervals"""

class SummaryRanges(object):
    # use heappush and heappop
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.res = []
        self.exist = set() # set() can store any types of data

    def addNum(self, val):
        """
        :type val: int
        :rtype: None
        """
        if val not in self.exist:
            heapq.heappush(self.res, [val, val])
        

    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """
        tmp = []
        while self.res:
            cur = heapq.heappop(self.res)
            if tmp and tmp[-1][1] + 1 >= cur[0]:
                tmp[-1][1] = max(tmp[-1][1], cur[1])
            else:
                tmp.append(cur)
        self.res = tmp
        return tmp











#
