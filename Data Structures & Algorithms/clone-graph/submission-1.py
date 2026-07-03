"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 
        res = []
        stack = []
        visited = set()
        clone = {}
        visited.add(node)
        stack.append(node)
        clone[node] = Node(node.val)
        start = clone[node]
        while stack:
            node = stack.pop()
            for n in node.neighbors:
                if n not in clone:
                    clone[n] = Node(n.val)
                if n not in visited:
                    visited.add(n)
                    stack.append(n) 
                clone[node].neighbors.append(clone[n])

        return start
     