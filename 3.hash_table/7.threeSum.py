class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        left, right = 0, len(nums)-1
        for i in range(len(nums)):
            if nums[i] > 0:
                return result
            if i > 0 and nums[i]==nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                _sum = nums[i]+nums[left]+nums[right]
                if _sum < 0:
                    left += 1
                elif _sum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while right>left and nums[left+1]==nums[left]:
                        left += 1
                    while right>left and nums[right-1]==nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
        return result

solution = Solution()
res = solution.threeSum([-1, 0, 1, 2, -1, -4])
print(res)
