class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        res = []
        for i in range(0,n):
            l,r = intervals[i]
            if newInterval[1] < l:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > r:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], l),
                    max(newInterval[1], r)
                ]
        res.append(newInterval)
        return res

        

        