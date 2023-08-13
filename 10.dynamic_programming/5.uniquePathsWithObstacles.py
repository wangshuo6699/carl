class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            if obstacleGrid[i][0]==0:
                dp[i][0] = 1
            else:
                break
        for j in range(n):
            if obstacleGrid[0][j]==0:
                dp[0][j] = 1
            else:
                break
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]==1:
                    continue
                dp[i][j] = dp[i][j-1]+dp[i-1][j]
        return dp[-1][-1]

solution = Solution()
res = solution.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
print(res)
