class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if abs(target)>sum(nums):
            return 0
        if (sum(nums)+target)%2!=0:
            return 0
        target_sum = (sum(nums)+target)//2
        dp =[[0]*(target_sum+1) for _ in range(len(nums)+1)]
        dp[0][0]=1
        for i in range(1, len(nums)+1):
            for j in range(target_sum+1):
                dp[i][j] = dp[i-1][j]
                if j >= nums[i-1]:
                    dp[i][j] += dp[i-1][j-nums[i-1]]
        return dp[-1][-1]


solution = Solution()
res = solution.findTargetSumWays([1,1,1,1,1], 3)
print(res)
