class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        ans = []
        for path in paths:
            path = path.split(" ")
            
            for j in range(1,len(path)):
                currentPath = path[j]
                directory = path[0]+"/"

                fileName, content = currentPath.split("(")
                directory += fileName

                if content not in d:
                    d[content] = []

                d[content].append(directory)

        for key in d:
            if len(d[key]) > 1:
                ans.append(d[key])

        return ans
            
