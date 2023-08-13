class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)
        for k in range(0, len(nums)-3):
            if nums[k]>target and target>0:
                continue
            if k>0 and nums[k]==nums[k-1]:
                continue
            for i in range(k+1, len(nums)-2):
                if nums[k]+nums[i]>target and target>0:
                    continue
                if i > k+1 and nums[i]==nums[i-1]:
                    continue
                left = i+1
                right = len(nums)-1
                while left<right:
                    if nums[k]+nums[i]+nums[left]+nums[right]==target:
                        res.append([nums[k], nums[i], nums[left], nums[right]])
                        while left<right and nums[left]==nums[left+1]:
                            left+=1
                        while left<right and nums[right]==nums[right-1]:
                            right-=1
                        left += 1
                        right -= 1
                    elif nums[k]+nums[i]+nums[left]+nums[right]<target:
                        left += 1
                    else:
                        right -= 1
        return res

solution = Solution()
solution.fourSum([-2,-1,-1,1,1,2,2], 0)
