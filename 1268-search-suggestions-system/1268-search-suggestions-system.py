class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        self.root = TrieNode()
        for word in products:
            self.insert(word)
        
        return self.search(searchWord)
    
    
    def insert(self, word):
        curr = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr.common.append(word)
            curr = curr.children[idx]
        curr.common.append(word)
    def search(self, word):
        curr = self.root
        st = []
        for char in word:
            idx = ord(char) - ord('a')
            if  curr.children[idx]:
              
                curr = curr.children[idx]
                st.append(sorted(curr.common)[:3])
            else:
                break
                
        remaining = len(word) - len(st)
        for j in range(remaining):
            st.append([])
        return st 
        
            


class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.common = []