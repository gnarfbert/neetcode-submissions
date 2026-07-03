class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(0, len(intervals)):
            l, r = intervals[i]
            if newInterval[1] < l:
                res.append(newInterval)    
                return res + intervals[i:]
            elif newInterval[0] > r:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(l, newInterval[0]),
                    max(r, newInterval[1])
                ]
        res.append(newInterval)
        return res
        
