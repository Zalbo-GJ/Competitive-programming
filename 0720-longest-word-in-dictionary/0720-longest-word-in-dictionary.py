class Solution:
    def longestWord(self, words: List[str]) -> str:
        self.root = TrieNode()
        self.root.is_end = True
        
        for word in words:
            self.insert(word)
        
        return self.search(self.root)

    def insert(self, word):
        curr = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        
        curr.is_end = True
    
    def search(self,curr):
    
        st = []
        for idx in range(26):
            node = curr.children[idx]
            if node and node.is_end:
                st.append((chr(idx + ord('a')))  + self.search(node))
        st.sort(key=lambda x: (-len(x), x))
        longest_smallest = max(st, key=len) if st else ""

        return longest_smallest
            
class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False