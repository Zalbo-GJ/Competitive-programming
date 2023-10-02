class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        root = TrieNode()
        self.ans = 0
        self.s = s
        for word in words:
            self.insert(root, word)
        
        
        self.search(root, 0)
        
        return self.ans
    
    def insert(self, root, word):
        curr = root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end += 1
    @cache
    def search(self, node, idx):
        self.ans+=node.is_end
        if not node.children:
            return
        for letter,n in node.children.items():
            for i in range(idx,len(self.s)):
                if self.s[i]==letter:
                    self.search(n,i+1)
                    break
        return
        

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = 0
