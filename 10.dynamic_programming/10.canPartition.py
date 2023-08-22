class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums)%2!=0:
            return False
        target = sum(nums)//2
        dp = [0] * (target+1)
        for i in nums:
            for j in range(target, -1, -1):
                if j<i:
                    continue
                dp[j] = max(dp[j], dp[j-i]+i)
        return dp[-1]==target

solution = Solution()
res = solution.canPartition([1, 5, 11, 5])
print(res)
