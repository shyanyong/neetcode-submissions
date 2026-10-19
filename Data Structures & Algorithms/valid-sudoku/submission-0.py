class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def rowChecker(row):
            print(row)
            seen = set()
            for val in row:
                if val != '.' and val in seen:
                    return False
                seen.add(val)
            return True

        def colChecker(index, board):
            seen = set()
            for row in board:
                val = row[index]
                if val != '.' and val in seen:
                    return False
                seen.add(val)
            return True

        def boxChecker(row, col):
            seen = set()
            for i in range(3):
                for j in range(3):
                    val = board[row + i][col + j]
                    if val != '.' and val in seen:
                        return False
                    seen.add(val)
            return True
        
        for i in range(9):
            if not rowChecker(board[i]):
                return False
            if not colChecker(i, board):
                return False
        
        for i in range(3):
            for j in range(3):
                if not boxChecker(i * 3, j * 3):
                    return False
        return True