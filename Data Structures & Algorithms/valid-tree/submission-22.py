class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != (n - 1):
            return False

        adjList = {key: [] for key in range(n)}

        for src, dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)
        
        def dfs(node, parent):

            # if node == parent:
            #     return True

            if node in path:# and node != parent:
                return False

            #print(node, adjList[node])
            path.add(node)

            for neighbor in adjList[node]:
    
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False

            return True

        path = set()

        try:
            node = edges[0][0]
        except:
            return True


        if not dfs(node, -1):
            return False
                
        #print(len(path), path)
        if len(path) != n:
            return False
        

        return True