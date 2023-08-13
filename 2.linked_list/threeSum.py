class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            if nums[i] > 0:
                continue
            left = i + 1
            right = len(nums)-1
            while left < right:
                if nums[i]+nums[left]+nums[right]==0:
                    if [nums[i], nums[left], nums[right]] not in result:
                        result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif nums[i]+nums[left]+nums[right]<0:
                    left += 1
                else:
                    right -=1
        return result
                

solution = Solution()
solution.threeSum([-1,0,1,2,-1,-4])
