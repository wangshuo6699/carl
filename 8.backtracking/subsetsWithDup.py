class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        def backtracking(nums, startindex, path):
            res.append(path[:])
            if startindex==len(nums):
                return
            for i in range(startindex, len(nums)):
                if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue
                path.append(nums[i])
                used[i]=True
                backtracking(nums, i+1, path)
                used[i]=False
                path.pop()
                
        used = [False]*len(nums)
        res, path = [], []
        backtracking(nums, 0, path)
        return res

solution = Solution()
solution.subsetsWithDup([4, 4, 4, 1, 4])
