class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        def dfs(node, parent):

            if node in path:
                return False

            path.add(node)

            for neighbor in adjList[node]:

                if neighbor == parent:
                    continue

                if not dfs(neighbor, node):
                    return False

            return True
        
        if len(edges) != n - 1:
            return False

        adjList = {key: [] for key in range(n)}

        for src, dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)

        path = set()

        try:
            node = edges[0][0]
        except:
            return True

        if not dfs(node, -1):
            return False

        if len(path) != n:
            return False

        return True

        