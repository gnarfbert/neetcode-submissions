"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key= lambda x:x.start)
        
        for i in range(0, len(intervals) - 1):
            start,end = intervals[i].start, intervals[i].end
            for j in range(i + 1, len(intervals)):
                ns, ne = intervals[j].start, intervals[j].end
                if ns >= end:
                    continue
                else:
                    return False
        return True

            