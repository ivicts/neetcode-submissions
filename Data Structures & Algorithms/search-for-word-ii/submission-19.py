class TrieNode:

    def __init__(self):
        self.children = {}
        self.isWord = False
        self.idx = -1

    def insert(self, word, i):
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True
        cur.idx = i

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
       
        ROWS, COLS = len(board), len(board[0])
        resList = []
        root = TrieNode()
        visit = set()

        def dfs(board, r, c, visit, node):
            nonlocal ROWS, COLS, resList, words

            if node.isWord:
                if node.idx != -1:
                    resList.append(words[node.idx])
                    node.idx = -1

            if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or board[r][c] not in node.children:
                return False

            visit.add((r, c))

            node = node.children[board[r][c]]

            res = (dfs(board, r - 1, c, visit, node)
            or dfs(board, r + 1, c, visit, node)
            or dfs(board, r, c - 1, visit, node)
            or dfs(board, r, c + 1, visit, node))
            
            visit.remove((r, c))

            return res

        for i in range(len(words)):
            root.insert(words[i], i)

        for r in range(ROWS):
            for c in range(COLS):
                dfs(board, r, c, visit, root)

        return resList

        
             