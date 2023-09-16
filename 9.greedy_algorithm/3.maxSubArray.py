class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        result = float('-inf')
        for num in nums:
            count += num
            if count>result:
                result = count
            if count<0:
                count = 0
        return result

solution = Solution()
res = solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(res)
