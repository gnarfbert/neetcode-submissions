class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        visited = set()
        for u,v,w in times:
            edges[u].append((v,w))
        
        minHeap = [(0,k)]
        minTime = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            minTime = w1
            for n2,w2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w2 + w1, n2))
        if len(visited) == n:
            return minTime
        else:
            return -1
