class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashset = set()
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] == ".":
                    continue
                row =  str(board[i][j]) + "_ROW_" + str(i) 
                col = str(board[i][j]) + "_COL_" + str(j) 
                box = str(board[i][j]) + "_BOX_" + str(i // 3) + "_" + str(j // 3)
                
                if row in hashset or col in hashset or box in hashset:
                    return False

                hashset.add(row)
                hashset.add(col)
                hashset.add(box)
        return True