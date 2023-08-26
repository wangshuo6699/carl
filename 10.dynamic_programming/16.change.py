class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # dp = [0]*(amount+1)
        # dp[0] = 1
        # for i in range(len(coins)):
        #     for j in range(coins[i], amount+1):
        #         dp[j] += dp[j-coins[i]]
        n = len(coins)
        dp = [[0]*(n+1) for _ in range(amount+1)]   # 初始化
        dp[0][0] = 1    # 合法的初始化
        
        # 完全背包：优化后的状态转移
        for i in range(amount+1):   # 第二层循环：遍历背包
            for j in range(1, n+1):         # 第一层循环：遍历硬币
                if i < coins[j-1]:      # 容量有限，无法选择第i个硬币
                    dp[i][j] = dp[i-1][j]
                else:                   # 可选择第i个硬币
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
        
        return dp[n][amount]
        # return dp[-1]

solution = Solution()
res = solution.change(5, [1, 2, 5])
print(res)
