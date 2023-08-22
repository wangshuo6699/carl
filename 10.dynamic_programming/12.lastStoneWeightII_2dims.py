class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        target = sum(stones)//2
        dp = [[0]*(target+1) for _ in range(len(stones))]
        dp[0][0] = 0
        for i in range(len(stones)):
            for j in range(1, target+1):
                if j<stones[i]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=max(dp[i-1][j], dp[i-1][j-stones[i]]+stones[i])
        return sum(stones)-dp[-1][-1]-dp[-1][-1]

solution = Solution()
res = solution.lastStoneWeightII([2,4,1,1])
print(res)
