class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        dp = [1]*len(nums)
        for i in range(1, len(nums)):
            for j in range(i-1, i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)


solution = Solution()
solution.findLengthOfLCIS([2,2,2,2,2])
