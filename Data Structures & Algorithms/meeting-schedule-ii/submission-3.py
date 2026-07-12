"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        hq = []
        intervals.sort(key=lambda x:x.start)
        for interval in intervals:
            if hq and interval.start >= hq[0]:
                heapq.heappop(hq)
            heapq.heappush(hq, interval.end)
        
        return len(hq)
