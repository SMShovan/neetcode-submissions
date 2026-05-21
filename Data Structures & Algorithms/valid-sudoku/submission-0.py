class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        seen = set()

        row = len(board)
        col = len(board[0])

        for r in range(row):
            for c in range(col):
                if board[r][c] == ".":
                    continue
                patternR = str('r') + str(r) + board[r][c];
                patternC = str('c') + str(c) + board[r][c];
                patternB = str('B') + str(r//3) + str(c // 3) + board[r][c];

                if patternR in seen or patternC in seen or patternB in seen:
                    return False
                seen.add(patternR)
                seen.add(patternC)
                seen.add(patternB)
                
        return True
                