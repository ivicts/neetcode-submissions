class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c, visit):
            nonlocal ROWS, COLS

            if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == "0":
                return

            grid[r][c] = "0"
            visit.add((r, c))

            res = (dfs(r - 1, c, visit)
            or dfs(r + 1, c, visit)
            or dfs(r, c - 1, visit)
            or dfs(r, c + 1, visit))

            visit.remove((r, c))

            return

        total_count = 0
        visit = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c, visit)
                    total_count += 1

        return total_count