class RandomizedSet:

    def __init__(self):
        self.dic = {}

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        
        self.dic[val] = 1
        return True

    def remove(self, val: int) -> bool:
        
        if val not in self.dic:
            return False
        
        self.dic.pop(val)
        return True
    
    def getRandom(self) -> int:
        
        if self.dic:
            keys = list(self.dic.keys())
            
            random_val = random.choice(keys)
            return random_val
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()