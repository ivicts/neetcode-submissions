"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def bfs(node):
            nonlocal oldToNew

            if node is None:
                return None
            visit = set()
            visit.add(node)
            cloneNode = Node(node.val)
            oldToNew[node] = cloneNode
            queue = deque()
            queue.append(node)

            while queue:
                for i in range(len(queue)):
                    curr = queue.popleft()
                    cloneNode = oldToNew[curr]
                    #print("A")
                    # if curr == target:
                    #     return length

                    for neighbor in curr.neighbors:
                        if neighbor not in oldToNew:
                            #visit.add(neighbor)
                            cloneNeighbor = Node(neighbor.val)
                            oldToNew[neighbor] = cloneNeighbor
                            queue.append(neighbor)
                        cloneNode.neighbors.append(oldToNew[neighbor])

            return oldToNew[node]

        return bfs(node)
                    
            