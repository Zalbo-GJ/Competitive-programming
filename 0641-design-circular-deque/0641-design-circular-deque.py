class MyCircularDeque:

    def __init__(self, k: int):
        self.que = Deque()
        self.k = k
        self.size = 0
        
        

    def insertFront(self, value: int) -> bool:
        if self.size < self.k:
            self.que.appendleft(value)
            self.size += 1
            return True
        return  False
        
        

    def insertLast(self, value: int) -> bool:
        if self.size < self.k:
            self.que.append(value)
            self.size += 1
            return True
        return  False


    def deleteFront(self) -> bool:
        if self.size > 0:
            self.que.popleft()
            self.size -= 1
            return True
        return False
        

    def deleteLast(self) -> bool:
        if self.size > 0:
            self.que.pop()
            self.size -= 1
            return True
        return False
        

    def getFront(self) -> int:
        if self.size > 0:
            return self.que[0]
        return -1
        

    def getRear(self) -> int:
        if self.size > 0:
            return self.que[-1]
        return -1
        

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.size == self.k:
            return True
        return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()