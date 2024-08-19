class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nums = [1,2,3,4,5,6,7,8,9]
        #row check
        for row in board:
            for num in nums:
                if row.count(str(num)) > 1:
                    return False
        
        #column check
        for i in range(9):
            column = []
            for row in board:
                column.append(row[i])
            for num in nums:
                if column.count(str(num)) > 1:
                    return False
        
        #squares check
        for i in range(3):
            for j in range(3):
                square = []
                for k in range(3):
                    for l in range(3):
                        square.append(board[(i*3)+k][(j * 3)+l])
                for num in nums:
                    if square.count(str(num)) > 1:
                        return False
        return True