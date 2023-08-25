class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for j in range(len(coins)):
                if i - coins[j] >= 0
                    print()
                if i - coins[j] >= 0 and dp[i - coins[j]] != float('inf'):
                    dp[i] = min(dp[i-coins[j]]+1, dp[i])
        if dp[-1]==float('inf'):
            return -1
        return dp[-1]

solution = Solution()
solution.coinChange([2147483647], 2)
solution.coinChange([1, 2, 5], 11)
