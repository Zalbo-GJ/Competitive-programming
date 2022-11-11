class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        
        d = []
        for i in range(len(names)):
            d.append((heights[i],names[i]))
            
        d.sort(key = lambda x : x,reverse = True)
        
        return [i[1] for i in d]