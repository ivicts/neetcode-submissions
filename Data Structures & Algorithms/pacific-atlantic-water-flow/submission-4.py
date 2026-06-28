class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        def bfs(heights, r, c, visit):
            nonlocal ROWS, COLS
            neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]

            queue = deque()
            if (r, c) not in visit:
                visit.add((r, c))
                queue.append((r, c))

            while queue:
    
                for i in range(len(queue)):
                    r, c = queue.popleft()

                    for dr, dc in neighbors:
                        nr, nc = r + dr, c + dc
                        if (min(nr, nc) < 0 or (nr, nc) in visit or
                            nr >= ROWS or nc >= COLS or heights[nr][nc] < heights[r][c]):
                            continue
                        queue.append((nr, nc))
                        visit.add((nr, nc))

            return visit

        pacific = set()
        atlantic = set()

        for r in range(ROWS):
            pacific = bfs(heights, r, 0, pacific)
            atlantic = bfs(heights, r, COLS - 1, atlantic)

        for c in range(COLS):
            pacific = bfs(heights, 0, c, pacific)
            atlantic = bfs(heights, ROWS - 1, c, atlantic)

        
        return list(pacific.intersection(atlantic))