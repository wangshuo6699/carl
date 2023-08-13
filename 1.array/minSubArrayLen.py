class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        sum = 0
        result = len(nums)+1
        for j in range(len(nums)):
            sum += nums[j]
            while sum >= target:
                sub_l = j - i + 1
                result = min(result, sub_l)
                sum -= nums[i]
                i += 1
        if result>len(nums):
            return 0
        return result


solution = Solution()
solution.minSubArrayLen(7, [2,3,1,2,4,3])
