class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        i = 0
        
        while i < len(image):
            start = 0
            end = len(image[i])-1
            while start <= end:
                if image[i][start] == 0: image[i][start] = 1
                else: image[i][start] = 0
                if start == end: break

                if image[i][end] == 0: image[i][end] = 1
                else: image[i][end] = 0
            
            
                image[i][start], image[i][end] = image[i][end], image[i][start]
                start+=1
                end-=1
            i+=1
        return image
            