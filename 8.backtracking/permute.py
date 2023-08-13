class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtracking(nums, used, path):
            if len(path)==len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtracking(nums, used, path)
                used[i] = False
                path.pop()
        
        used = [False] * len(nums)
        res, path = [], []
        backtracking(nums, used, path)
        return res
    
solution = Solution()
solution.permute([1, 2, 3])
