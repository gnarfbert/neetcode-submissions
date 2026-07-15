class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            start, end = intervals[i]
            if newInterval[0] > end:
                res.append(intervals[i])
            elif start > newInterval[1]:
                res.append(newInterval)
                print(intervals[i:])
                return res + intervals[i:]
            else:
                newInterval = [
                    min(start, newInterval[0]),
                    max(end, newInterval[1])
                ]
        print(newInterval)
        res.append(newInterval)
        return res



        