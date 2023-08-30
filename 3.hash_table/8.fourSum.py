class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        for i in range(len(nums)-3):
            if nums[i] > target and target>0:
                return result
            if i > 0 and nums[i-1]==nums[i]:
                continue
            for j in range(i+1, len(nums)-2):
                if nums[i]+nums[j]>target and target>0:
                    break
                if j > i+1 and nums[j-1]==nums[j]:
                    continue
                left = j+1
                right = len(nums)-1
                while left<right:
                    _sum = nums[i]+nums[j]+nums[left]+nums[right]
                    if _sum < target:
                        left+=1
                    elif _sum > target:
                        right -= 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left<right and nums[left+1]==nums[left]:
                            left+=1
                        while left<right and nums[right-1]==nums[right]:
                            right -= 1
                        left+=1
                        right -= 1
        return result

solution = Solution()
res = solution.fourSum(nums=[-9,-2,7,6,-8,5,8,3,-10,-7,8,-8,0,0,1,-8,7], target=4)
print(res)
