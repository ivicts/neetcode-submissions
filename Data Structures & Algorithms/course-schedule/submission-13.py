class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = {key: [] for key in range(numCourses)}

        for src, dst in prerequisites:
            adjList[src].append(dst)
        
        visited = set()
        path = set()

        def dfs(node):

            if node in visited:
                return True

            if node in path:
                return False

            path.add(node)

            for neighbor in adjList[node]:
                if not dfs(neighbor):
                    return False

            visited.add(node)
            path.remove(node)
            
            return True

        for node in range(numCourses):
            if node not in visited:
                if not dfs(node):
                    return False
            
        return True
            