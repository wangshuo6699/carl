class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        pre_max = self.robRange(nums[:-1])
        pos_max = self.robRange(nums[1:])
        return max(pre_max, pos_max)
    
    def robRange(self, nums):
        if len(nums)==1:
            return nums[0]
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]

solution = Solution()
res = solution.rob([1,2,3])
print(res)
