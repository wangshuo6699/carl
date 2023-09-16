class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        conver = 0
        if len(nums)<2:
            return True
        for i in range(conver):
            conver = max(i+nums[i], conver)
            if conver>=(len(nums)-1):
                return True
        return False

solution = Solution()
res = solution.canJump([2,3,1,1,4])
print(res)
