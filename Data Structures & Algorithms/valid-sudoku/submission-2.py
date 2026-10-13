class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        seen = set()

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                
                row = "r" + str(r) + board[r][c];
                col = "c" + str(c) + board[r][c];
                box = "b" + str(r//3) + str(c//3) + board[r][c];

                if row in seen or col in seen or box in seen:
                    return False
                
                seen.add(row)
                seen.add(col)
                seen.add(box)
                
        return True


# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
        
#         seen = set()

#         row = len(board)
#         col = len(board[0])

#         for r in range(row):
#             for c in range(col):
#                 if board[r][c] == ".":
#                     continue
#                 patternR = str('r') + str(r) + board[r][c];
#                 patternC = str('c') + str(c) + board[r][c];
#                 patternB = str('B') + str(r//3) + str(c // 3) + board[r][c];

#                 if patternR in seen or patternC in seen or patternB in seen:
#                     return False
#                 seen.add(patternR)
#                 seen.add(patternC)
#                 seen.add(patternB)
                
#         return True
                