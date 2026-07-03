class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        edges = collections.defaultdict(list)
        for src, dst, delay in times:
            edges[src].append((dst, delay))
        pq = [(0, k)]
        minTime = 0
        visited = set()
        while pq:
            w1, n1 = heapq.heappop(pq)
            if n1 in visited:
                continue
            minTime = w1
            visited.add(n1)
            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(pq, (w1 + w2, n2))
                
        
        if len(visited) == n:
            return minTime
        else:
            return -1


        