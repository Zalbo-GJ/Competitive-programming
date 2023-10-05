class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        self.root = TrieNode()
        ans = []
        for word in words:
            self.insert(word)
        
        for word in words:
            ans.append(self.search(word))

        return ans
    
    def insert(self, word):
        curr = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if  not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
            curr.val += 1
    
    def search(self, word):
        curr = self.root
        ans = 0
        for char in word:
            idx = ord(char) - ord('a')
            curr = curr.children[idx]
            ans += curr.val
        return ans

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.val = 0