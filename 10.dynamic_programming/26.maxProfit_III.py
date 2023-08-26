class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [[0, 0, 0, 0] for _ in prices]
        dp[0][0] = -prices[0]
        dp[0][2] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1]-prices[i])
            dp[i][3] = max(dp[i-1][3], dp[i-1][2]+prices[i])
        return dp[-1][-1]

solution = Solution()
solution.maxProfit([3,3,5,0,0,3,1,4])
