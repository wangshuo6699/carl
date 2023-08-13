class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for j in range(n)] for i in range(m)]
        for i in range(len(dp)):
            dp[i][0] = 1
        for j in range(len(dp[0])):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]

solution = Solution()
solution.uniquePaths(3, 7)
