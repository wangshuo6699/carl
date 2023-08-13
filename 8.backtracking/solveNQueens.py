class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        path = [['.']*n for _ in range(n)]
        def isValid(checkerboard, row, col):
            for line in checkerboard:
                if line[col]=='Q':
                    return False
            i = row - 1
            j = col - 1
            while i>=0 and j>=0:
                if checkerboard[i][j]=='Q':
                    return False
                i -= 1
                j -= 1
            
            i = row - 1
            j = col + 1
            while i>=0 and j<n:
                if checkerboard[i][j]=='Q':
                    return False
                i -= 1
                j += 1
            return True

        def backtracking(checkerboard, row, n):
            if row == n:
                res.append([''.join(_) for _ in checkerboard])
                return
            for col in range(n):
                if isValid(checkerboard, row, col):
                    checkerboard[row][col]='Q'
                    backtracking(checkerboard, row+1, n)
                    checkerboard[row][col]='.'
        
        backtracking(path, 0, n)
        return res

solution = Solution()
solution.solveNQueens(4)
