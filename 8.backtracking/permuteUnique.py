class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res, path = [], []
        used = [False] * len(nums)
        def backtracking(nums, path):
            if len(path)==len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtracking(nums, path)
                used[i]=False
                path.pop()
        
        backtracking(nums, path)
        return res
    
solution = Solution()
solution.permuteUnique([1,2,3])
