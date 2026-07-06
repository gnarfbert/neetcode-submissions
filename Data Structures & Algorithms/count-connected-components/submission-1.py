class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0

        adjList = collections.defaultdict(set)

        seen = set()
        for src, dst in edges:
            adjList[src].add(dst)
            adjList[dst].add(src)
        
        def bfs(u):
            q = []
            q.append((u, None))

            while q:
                node, parent = q.pop(0)
                if node not in seen:
                    seen.add(node)
                
                for neigh in adjList[node]:
                    if neigh == parent:
                        continue
                    
                    if neigh in seen:
                        continue
                    
                    q.append((neigh,node))
                    seen.add(neigh)
        
        for i in range(0,n):
            if i not in seen:
                print(i)
                bfs(i)
                res += 1
        
        return res



        