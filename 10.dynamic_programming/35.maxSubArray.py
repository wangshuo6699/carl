class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return nums[0]
        dp = [0]*len(nums)
        dp[0] = nums[0]
        max_num = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            max_num = max(dp[i], max_num)
        return max_num

solution = Solution()
res = solution.maxSubArray([-1,-2])
print(res)
