class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:

        left = {i: {1,4,6} for i in [1,3,5]}
        right = {i:[1,3,5]  for i in [1,4,6]}
        up = {i:[2,3,4] for i in [2,5,6]}
        down = {i:[2,5,6] for i in [2,3,4] }
        cols= len(grid[0])
        rows= len(grid)
        rep = {}
        for row in range(rows):
            for col in range(cols):
                rep[(row,col)] = (row,col)
                
        def find(node):
            if rep[node] != node:
                rep[node] = find(rep[node])
            return rep[node]
        
        def union(x, y):
            xrep = find(x)
            yrep = find(y)
            
            if xrep!=yrep:
                rep[yrep] = xrep
        
        dirr = {}
        for row in range(rows):
            for col in range(cols):
                if row == 0 and col == 0:
                    continue
                if row + 1 < rows and grid[row][col] in down and grid[row + 1][col] in down[grid[row][col]]:
                    union((row,col),(row+1,col))
                if row -1 >= 0 and grid[row][col] in up and  grid[row - 1][col] in up[grid[row][col]]:
                    union((row,col),(row-1,col))
                if col + 1 < cols and grid[row][col] in right and grid[row][col+1] in right[grid[row][col]]:
                    union((row,col),(row,col+1))
                if col - 1 >=0 and grid[row][col] in left and  grid[row][col-1] in left[grid[row][col]]:
                    union((row,col),(row,col-1))

        return find((rows-1,cols-1)) == find((0,0))