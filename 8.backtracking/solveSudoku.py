class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def isValid(board, row, col, i):
            for j in board[row]:
                if j==i:
                    return False
            
            for j in range(len(board)):
                if board[j][col]==i:
                    return False
            
            startRow = (row//3)*3
            startCol = (col//3)*3
            for j in range(3):
                for k in range(3):
                    if board[startRow+j][startCol+k]==i:
                        return False
            return True
        
        def backtracking(board):
            for row in range(len(board)):
                for col in range(len(board[0])):
                    if board[row][col]!='.': continue
                    for i in range(1,10):
                        i = str(i)
                        if isValid(board, row, col, i):
                            board[row][col]=i
                            if backtracking(board):
                                return True
                            board[row][col]='.'
                    return False
            return True
        
        backtracking(board)
        return board


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
solution = Solution()
solution.solveSudoku(board)
