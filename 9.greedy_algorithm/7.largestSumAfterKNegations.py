class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums, key=lambda x:abs(x), reverse=True)
        for i in range(len(nums)):
            if nums[i]<0:
                if k>0:
                    nums[i] = -nums[i]
                    k -= 1
        if k>0:
            for j in range(len(nums)-1, -1, -1):
                if k > 0:
                    nums[j] = -nums[j]
                    k -= 1
        return sum(nums)

solution = Solution()
res = solution.largestSumAfterKNegations([4,2,3], k = 1)
print(res)
