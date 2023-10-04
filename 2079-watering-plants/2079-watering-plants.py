class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
             
        count = 0
        bucket = capacity
        for i, plant in enumerate(plants):
            if plant <= bucket:
                count += 1
            else:
                count += i
                bucket = capacity
                count += (i + 1)
                
            bucket -= plant

        return (count)