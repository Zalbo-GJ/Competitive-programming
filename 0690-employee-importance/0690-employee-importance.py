"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        def dfs(emp):
            nonlocal importance
            importance = emp.importance
            for sub in emp.subordinates:
                importance +=  dfs(dic[sub])
            
            return importance
        
        
        dic = {}
        importance = 0
        for emp in employees:
            dic[emp.id] = emp
        
        return dfs(dic[id])