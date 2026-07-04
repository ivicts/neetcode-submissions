class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adjList = {key: [] for key in range(n)}

        for src, dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)

        def dfs(node):
            if node in path:
                return True

            path.add(node)

            for neighbor in adjList[node]:
                dfs(neighbor)

            #path.remove(node)

            return False

        path = set()
        res = 0 

        for node in range(n):
            if node not in path:
                dfs(node)
                res += 1

        return res