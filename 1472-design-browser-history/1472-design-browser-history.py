class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None  
        self.prev = None
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.head.next = None
        self.head.prev = None
        self.curr = self.head
        
    
    def visit(self, url: str) -> None:
        node = Node(url)
        
        self.curr.next = node
        node.prev = self.curr
        self.curr = self.curr.next
    

    def back(self, steps: int) -> str:
        
        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val
        

    def forward(self, steps: int) -> str:
        
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)