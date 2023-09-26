class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        curr = self.root
        
        for char in key:
            idx = ord(char) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            
            curr = curr.children[idx]
        curr.num = val
        

    def sum(self, prefix: str) -> int:
        curr = self.root
        
        for char in prefix:
            idx = ord(char) - ord('a')
            if not curr.children[idx]:
                return 0
            curr = curr.children[idx]
                
        return self.dfs(curr)
    
    def dfs(self, node):
        if not node:
            return 0
        
        arr = []
        for n in node.children:              
                arr.append(self.dfs(n))
    
        return node.num + sum(arr)
        
class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.num = 0

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)