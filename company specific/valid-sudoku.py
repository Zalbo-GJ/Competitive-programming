class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [[set() for _ in range(3)] for _ in range(9)]
        
        for row in range(9):
            for col in range(9):
                
                cell = board[row][col]
                
                if cell != ".":
                    if cell in rows[row] or cell in cols[col] or cell in squares[row//3][col//3]:
                        return False

                    rows[row].add(cell)
                    cols[col].add(cell)
                    squares[row // 3][col // 3].add(cell)

        
        return True
        