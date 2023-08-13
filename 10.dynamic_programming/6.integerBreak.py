class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(1, i//2+1):
                dp[i] = max(dp[i], max((i-j)*j, dp[i-j]*j))
        return dp[-1]

solution = Solution()
res = solution.integerBreak(10)
print(res)
