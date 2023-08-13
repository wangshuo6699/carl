class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtracking(nums, startindex, path):
            res.append(path[:])
            if startindex==len(nums):
                return
            for i in range(startindex, len(nums)):
                path.append(nums[i])
                backtracking(nums, i+1, path)
                path.pop()
        
        res, path = [], []
        backtracking(nums, 0, path)
        return res

solution = Solution()
solution.subsets([1,2,3])
