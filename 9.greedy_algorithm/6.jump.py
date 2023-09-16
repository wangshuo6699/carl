class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return 1
        cur = 0
        next = 0
        result = 0
        for i in range(len(nums)):
            next = max(next, i + nums[i])
            if i==cur:
                result += 1
                cur = next
                if cur==len(nums)-1:
                    return result
        return result

solution = Solution()
solution.jump([2,3,1,1,4])
