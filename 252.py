"""252. Meeting Rooms
given an array of meeting time intervals consisting of star and end times
determine if a person could attend all meetings."""
import heapq
class solution(object):
    def meetingRooms(self, intervals):
        intervals.sort()
        room = []
        for intv in intervals:
            if not room:
                room.append(intv[1])
            elif room and intv[0] < room[0]:
                return False
            elif room and intv[0] > room[0]:
                room.pop()
                room.append(intv[1])
        return True

s = solution()
res = s.meetingRooms([])
print(res)






















#############
