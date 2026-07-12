"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        
        rooms = [-1]
        intervals.sort(key=lambda x:x.start)
        for interval in intervals:
            start, end = interval.start, interval.end
            for i, prev in enumerate(rooms):
                if start >= prev:
                    rooms[i] = end
                    break
                else:
                    rooms.append(end)
                    break
            print(rooms)
            rooms.sort()
        return len(rooms)
        
        