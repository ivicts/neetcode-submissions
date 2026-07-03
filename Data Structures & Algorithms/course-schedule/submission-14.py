class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = {key: [] for key in range(numCourses)}

        for src, dst in prerequisites:
            adjList[src].append(dst)
        
        # visited = set()
        path = set()

        def dfs(node):

            if node in path:
                return False

            path.add(node)

            for neighbor in adjList[node]:
                if not dfs(neighbor):
                    return False

            adjList[node] = []
            path.remove(node)
            
            return True

        for node in range(numCourses):
            if not dfs(node):
                return False
        
        return True
            