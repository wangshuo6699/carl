class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 贪心算法
        # if len(nums)<=1:
        #     return len(nums)
        # result = 1
        # preDiff = 0
        # curDiff = 0
        # for i in range(len(nums)-1):
        #     curDiff = nums[i+1]-nums[i]
        #     if (preDiff<=0 and curDiff>0) or (preDiff>=0 and curDiff<0):
        #         result += 1
        #         preDiff = curDiff
        # return result

        # 动态规划算法
        dp = [[0]*2 for _ in nums]
        dp[0][0] = 1
        dp[0][1] = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i][0] = max(dp[i][0], dp[j][1]+1)
            for j in range(i):
                if nums[j]>nums[i]:
                    dp[i][1] = max(dp[i][1], dp[j][0]+1)
        return max(dp[-1][0], dp[-1][1])


solution = Solution()
res = solution.wiggleMaxLength([1,2,2,2,2,1])
print(res)
