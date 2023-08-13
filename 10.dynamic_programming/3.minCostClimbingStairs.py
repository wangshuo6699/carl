from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*len(cost)
        dp[0]=cost[0]
        dp[1]=cost[1]
        if len(cost)<=2:
            return min(cost[0], cost[1])
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1], dp[i-2])+cost[i]
        print(dp)
        return min(dp[-1], dp[-2])

solution = Solution()
solution.minCostClimbingStairs([10,15,20])
