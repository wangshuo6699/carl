class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums)%2!=0:
            return False
        target = sum(nums)//2
        dp = [[0]*(target+1) for _ in range(len(nums))]
        for i in range(len(dp)):
            dp[i][0]=0
        for i in range(len(nums)):
            for j in range(1, target+1):
                if j < nums[i]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=max(dp[i-1][j], dp[i-1][j-nums[i]]+nums[i])
        return dp[-1][-1]==target

solution = Solution()
res = solution.canPartition([1,5,11,5])
print(res)
