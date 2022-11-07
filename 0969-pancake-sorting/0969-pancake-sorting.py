class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        result = []
        i = len(arr)-1
        # i is current sorted border
        while i>=0:
            max_index = arr[0:i+1].index(max(arr[0:i+1]))
            
            if max_index == i:
                pass
            else:
                #swap to first ele
                arr[:max_index+1] = arr[0:max_index+1][::-1]
                result.append(max_index+1)
                arr[:i+1] = arr[0:i+1][::-1]
                # Swap the element to the largest pos available
                result.append(i+1)
            i-=1
        
        return result