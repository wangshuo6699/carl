class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        dp = [[0 for j in range(2*k+1)] for j in prices]
        for j in range(1, 2*k+1, 2):
            dp[0][j] = -prices[0]
        for i in range(1, len(prices)):
            for j in range(1, 2*k+1):
                if j%2==1:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]-prices[i])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]+prices[i])
        return dp[-1][-1]

solution = Solution()
solution.maxProfit(2, [1, 2, 3, 4, 5])
