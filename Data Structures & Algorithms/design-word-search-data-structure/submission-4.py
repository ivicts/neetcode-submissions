class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.root
        
        def dfs(word, curr):
            for i in range(len(word)):
                c = word[i]
                if c == ".":
                    possibleChars = list(curr.children.keys())
                    for possibleChar in possibleChars:
                        new_word = possibleChar + word[i + 1:]
                        #print(new_word)
                        if dfs(new_word, curr):
                            return True
                    return False
                elif c not in curr.children:
                    return False
                elif c in curr.children:
                    curr = curr.children[c]
            return curr.word
        
        return dfs(word, self.root)