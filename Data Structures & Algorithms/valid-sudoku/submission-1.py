class Solution:
    def isValidRow(self, board, row):
        seen = defaultdict(int)
        actual_row = board[row]
        for val in actual_row:
            if val == '.':
                continue
            if val in seen:
                return False
            seen[val] += 1
        return True
    
    def isValidCol(self, board, col):
        seen = defaultdict(int)
        for row in board:
            val = row[col]
            if val == '.':
                continue
            if val in seen:
                return False
            seen[val] += 1
        return True

    def isValidSquare(self, board, square):
        seen = defaultdict(int)
        if square < 4:
            row = {0, 1, 2}
        if 3 < square < 7:
            row = {3, 4, 5}
        if square > 6:
            row = {6, 7, 8}
        
        if square % 3 == 1:
            col = {0, 1, 2}
        
        if square % 3 == 2:
            col = {3, 4, 5}
        
        if square % 3 == 0:
            col = {6, 7, 8}
            
        for i in row:
            for j in col:
                val = board[i][j]
                if val == '.':
                    continue
                if val in seen:
                    return False
                seen[val] += 1
        return True
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = True
        for i in range(9):
            res = res and self.isValidRow(board, i)
            res = res and self.isValidCol(board, i)
            res = res and self.isValidSquare(board, i)
        return res
        