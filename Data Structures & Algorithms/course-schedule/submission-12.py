class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []



class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    
        adjList = {key: [] for key in range(numCourses)}

        for src, dst in prerequisites:
            if src == dst:
                return False
            adjList[src].append(dst)
        

        def dfs(node):#, adjList, visited):

            if node in path:
                return False

            if node in visited:
                return True

            path.add(node)

            for neighbor in adjList[node]:
                if not dfs(neighbor):#, adjList, visited):
                    return False

            #del adjList[node]
            #path.add(node)
            visited.add(node)
            path.remove(node)
            
            return True
        
        visited = set()
        path = set()
        for node in range(numCourses):
            #print(node)
            if node not in visited:
                if not dfs(node):#, adjList, visited):
                    return False

        return True

        
