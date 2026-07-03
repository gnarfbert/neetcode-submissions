class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        adj = collections.defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        visit = set()
        q = deque([(0, -1)])  # (current node, parent node)
        visit.add(0)

        while q:
            node, parent = q.popleft()
            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei in visit:
                    return False
                visit.add(nei)
                q.append((nei, node))

        return len(visit) == n