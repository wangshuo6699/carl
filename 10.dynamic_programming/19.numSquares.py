class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for j in range(1, int(i**(1/2))+1):
                if i>=j:
                    dp[i] = min(dp[i], dp[i-j*j]+1)
        return dp[-1]

solution = Solution()
res = solution.numSquares(12)
print(res)
