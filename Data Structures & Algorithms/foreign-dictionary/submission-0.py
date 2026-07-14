class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Creates an adjacency list of a graph where each char is a node
        # Avoid using defaultdict here because it will not create a node
        # for each unique character.
        adj = {c: set() for w in words for c in w}

        res = []

        for i in range(0, len(words) - 1):
            a = words[i]
            b = words[i + 1]
            minLen = min(len(a), len(b))
            if len(a) > len(b) and a[:minLen] == b[:minLen]:
                return ""
            
            for j in range(0, minLen):
                if a[j] != b[j]:
                    adj[a[j]].add(b[j])
                    break
        print(adj)  
        visited = {}

        def dfs(char):
            if char in visited:
                return visited[char]
            
            visited[char] = True
        
            for neigh in adj[char]:
                if dfs(neigh):
                    return True
            
            visited[char] = False
            res.append(char)
        
        for c in adj:
            if dfs(c):
                return ""
        
        res.reverse()
        return "".join(res)

        