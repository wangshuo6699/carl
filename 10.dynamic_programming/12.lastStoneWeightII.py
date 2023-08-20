class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        target = sum(stones)//2
        dp = [0]*(30*100//2+1)
        for i in range(len(stones)):
            for j in range(target, stones[i]-1, -1):
                dp[j] = max(dp[j], dp[j-stones[i]]+stones[i])
        return sum(stones)-2*dp[target]

solution = Solution()
res = solution.lastStoneWeightII([31,26,33,21,40])
print(res)
