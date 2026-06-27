"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        res = {}

        def dfs(node):
            nonlocal res

            if node in res:
                return res[node]

            if node is None:
                return None

            cloneNode = Node(val = node.val)
            res[node] = cloneNode

            for neighbor in node.neighbors:
                cloneNode.neighbors.append(dfs(neighbor))

            return cloneNode
        
        return dfs(node)