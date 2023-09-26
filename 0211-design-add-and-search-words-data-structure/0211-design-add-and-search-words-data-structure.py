class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            
            idx = ord(char) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            
            curr = curr.children[idx]
        curr.is_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        self.ans = False
        self.dfs(curr, word)
        return self.ans
    
    def dfs(self, curr, word):
        if not word:
            if curr.is_word:
                self.ans = True
            return 
        if word[0] == ".":
            for i in curr.children:
                if i:
                    self.dfs(i, word[1:])
        else:
            idx = ord(word[0]) - ord('a')
            if not curr.children[idx]:
                return
            self.dfs(curr.children[idx], word[1:])
        

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_word = False
        
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)