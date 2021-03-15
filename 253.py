"""253. Meeting Rooms II """
"""Given an array of meeting time intervals consisting of
start and end times [[s1,e1],[s2,e2],…] (si < ei), find the minimum number
of conference rooms required.
"""
import heapq
class Solution(object):
    def meetingRooms(self, intervals):
        """input type: List[List]
        rtype: int"""
        # O(nlogn)
        intervals.sort()
        heap = []
        for intv in intervals:
            print(heap)
            if heap and intv[0] >= heap[0]:
                heapq.heappushpop(heap, intv[1])

            else:
                heapq.heappush(heap, intv[1])
        return len(heap)

s = Solution()
res = s.meetingRooms([[0, 30],[18, 25], [5, 10],[15, 20]])
print(res)









######
