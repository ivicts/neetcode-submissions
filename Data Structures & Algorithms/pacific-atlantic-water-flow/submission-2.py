class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        
        resList = []

        def dfs(r, c, visit, prevHeights):
            nonlocal ROWS, COLS
            if (min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in visit or heights[r][c] < prevHeights):
                return False

            count = 0
            visit.add((r, c))

            prevHeights = heights[r][c]
            #res = set()

            res = ((dfs(r - 1, c, visit, prevHeights) or
                dfs(r + 1, c, visit, prevHeights) or
                dfs(r, c - 1, visit, prevHeights)) or
                dfs(r, c + 1, visit, prevHeights))
            
            #visit.remove((r, c))
            
            return res

        for c in range(COLS):
            dfs(0, c, pacific, 0)
            dfs(ROWS - 1, c, atlantic, 0)
        
        for r in range(COLS):
            dfs(r, 0, pacific, 0)
            dfs(r, COLS - 1, atlantic, 0)


        return list(pacific.intersection(atlantic))