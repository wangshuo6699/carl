class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        loop = n//2
        count = 0
        offset = 1
        startx, starty = 0, 0
        res = [[0 for i in range(n)] for j in range(n)]
        while loop>0:
            for j in range(starty, n-offset):
                count += 1
                res[startx][j] = count
            j += 1
            for i in range(startx, n-offset):
                count += 1
                res[i][j] = count
            i += 1
            for y in range(j, startx, -1):
                count += 1
                res[i][y] = count
            y -= 1
            for x in range(i, startx, -1):
                count += 1
                res[x][y] = count
            loop -= 1
            startx += 1
            starty += 1
            offset += 1
        if n%2==1:
            count += 1
            res[startx][starty] = count
        return res

solution = Solution()
solution.generateMatrix(5)
