class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visit = set()

        def dfs(board, r, c, visit, word_idx):
            nonlocal ROWS, COLS, word

            if (min(r, c) < 0 or r == ROWS or c == COLS or
                (r, c) in visit or board[r][c] == 1 or board[r][c] != word[word_idx]):
                return 0

            #if r == ROWS - 1 and c == COLS - 1:
            elif board[r][c] == word[word_idx]:
                
                if word_idx < len(word) - 1:
                    visit.add((r, c))
                    
                    count = 0
                    word_idx += 1
                    count += dfs(board, r - 1, c, visit, word_idx)
                    count += dfs(board, r + 1, c, visit, word_idx)
                    count += dfs(board, r, c - 1, visit, word_idx)
                    count += dfs(board, r, c + 1, visit, word_idx)

                    visit.remove((r, c))

                    return count
                else:
                    return 1

            else:
                return 0

        total_count = 0
        for r in range(ROWS):
            for c in range(COLS):
                total_count += dfs(board, r, c, visit, 0)
                if total_count > 0:
                    return True

        return False