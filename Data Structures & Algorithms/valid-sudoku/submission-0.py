class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_count = [{} for _ in range(9)]
        col_count = [{} for _ in range(9)]
        box_count = [{} for _ in range(9)]

        for row in range(9):
            for col in range(9):
                ch = board[row][col]
                
                if ch == ".":
                    continue
                
                box_id = (row//3)*3 + (col//3)
                
                if ch in row_count[row]:
                    return False
                if ch in col_count[col]:
                    return False
                if ch in box_count[box_id]:
                    return False
                
                row_count[row][ch] = 1
                col_count[col][ch] = 1
                box_count[box_id][ch] = 1

        return True