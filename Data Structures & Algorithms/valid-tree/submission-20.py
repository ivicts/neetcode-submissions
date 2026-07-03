class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != (n - 1):
            return False

        adjList = {key: [] for key in range(n)}

        for src, dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)
            # if src < dst:
            #     adjList[src].append(dst)
            # else:
            #     adjList[dst].append(src)
        #print(adjList)
        def dfs(node, parent):

            # if node == parent:
            #     return True

            if node in path:# and node != parent:
                print(node, parent)
                return False

            print(node, adjList[node])
            path.add(node)

            for neighbor in adjList[node]:
                # if parent == -1:
                #     parent = node
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False

            #adjList[node] = []
            #path.remove(node)

            return True

        path = set()

        
        #for node in range(n):
        try:
            node = edges[0][0]
        except:
            return True

        #for node in range(n):
        #if node not in path:
        if not dfs(node, -1):
            return False
                
        print(len(path), path)
        if len(path) != n:
            return False
        

        return True