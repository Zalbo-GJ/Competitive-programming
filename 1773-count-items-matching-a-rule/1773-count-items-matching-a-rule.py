class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        dix = {"type": 0, "color": 1, "name": 2}
        
        rule_idx = dix[ruleKey]
        match = 0
        for item in items:
            if item[rule_idx] == ruleValue:
                match += 1
        
        return match
        