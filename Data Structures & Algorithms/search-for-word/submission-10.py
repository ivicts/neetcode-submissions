class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visit = set()

        def dfs(board, r, c, visit, word_idx):
            nonlocal ROWS, COLS, word

            if word_idx == len(word):
                return True

            if (min(r, c) < 0 or r == ROWS or c == COLS or
                (r, c) in visit or board[r][c] == 1 or board[r][c] != word[word_idx]):
                return False

            visit.add((r, c))
            
            word_idx += 1
            res = (
                dfs(board, r - 1, c, visit, word_idx) or
                dfs(board, r + 1, c, visit, word_idx) or
                dfs(board, r, c - 1, visit, word_idx) or
                dfs(board, r, c + 1, visit, word_idx)
            )

            visit.remove((r, c))

            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(board, r, c, visit, 0):
                    return True

        return False