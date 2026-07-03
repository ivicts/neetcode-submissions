class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []



class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    
        adjList = {key: [] for key in range(numCourses)}

        for src, dst in prerequisites:
            # if src not in adjList:
            #     adjList[src] = []
            # if dst not in adjList:
            #     adjList[dst] = []
            if src == dst:
                return False
            adjList[src].append(dst)
        

        def dfs(node, adjList, visit, path):
            
            if node in path:
                return False
            
            if node in visit:
                return True

            #res = True
            path.add(node)
           

            for neighbor in adjList[node]:
                if not dfs(neighbor, adjList, visit, path):
                    return False

            path.remove(node)
            visit.add(node)
            return True

        try:
            node = prerequisites[0][0]
        except:
            return True
        
        visit = set() # Global visited
        path = set()  # Nodes in current recursion stack
        for node in range(numCourses):
            if node not in visit:
                if not dfs(node, adjList, visit, path):
                    return False

        return True