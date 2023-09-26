class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        self.root = TrieNode()
        self.insert(strs[-1])
        pre = []
        for i in range(0, len(strs)-1):
            pre.append(self.search(strs[i]))
        pre.sort()
        return pre[0]
            
    
    def insert(self, word):
        curr = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            
            curr = curr.children[idx]
    def search(self, word):
        curr = self.root
        st = []
        for char in word:
            idx = ord(char) - ord('a')
            if not curr.children[idx]:
                return "".join(st)
            curr = curr.children[idx]
            st.append(char)
        return "".join(st)
        

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        