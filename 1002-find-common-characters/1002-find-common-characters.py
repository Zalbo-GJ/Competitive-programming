class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        
        """
            step1: save count for each word in a dictionary 
            step2: for the  letter count of the first word take the min count in each word
            Step3: append the letter count times
            
        """
        counts = []
        
        for word in words:
            counts.append(Counter(word))
        ans = []
        for letter in counts[0]:
            minn = float("inf")
            
            for count in counts:
                
                minn = min(minn, count.get(letter, 0))
                
            for _ in range(minn):
                ans.append(letter)
        
        return ans
            
                
            
        
        