class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf')] * n

        dist[k - 1] = 0

        for _ in range(n-1):
            for src, dst, delay in times:
                if dist[src - 1] + delay < dist[dst - 1]:
                    dist[dst - 1] = dist[src - 1] + delay
        
        maxDist = max(dist)

        if maxDist < float('inf'):
            return maxDist
        else:
            return -1
        