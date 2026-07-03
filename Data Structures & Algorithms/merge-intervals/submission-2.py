class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        if len(intervals) == 1:
            return [intervals[0]]
        res = []
        pq = []
        intervals.sort()
        left, right = intervals[0]

        for i in range(1, len(intervals)):
            heapq.heappush(pq,intervals[i])

        while pq:
            nleft, nright = heapq.heappop(pq)
            if right < nleft:
                res.append([left, right])
                left = nleft
                right = nright
            elif nright < left:
                res.append([left,right])
                left = nleft
                right = nright
            else:
                left = min(left, nleft)
                right = max(right, nright)
        res.append([left,right])
        return res
        