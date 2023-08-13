class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtracking(nums, startindex, path):
            if len(path)>1:
                res.append(path[:])
            if startindex==len(nums):
                return
            
            used = set()
            for i in range(startindex, len(nums)):
                if path and nums[i]<path[-1]:
                    continue
                # if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                if nums[i] in used:
                    continue
                used.add(nums[i])
                # used[i]=True
                path.append(nums[i])
                backtracking(nums, i+1, path)
                path.pop()
        used = [True]*len(nums)
        res, path = [], []
        backtracking(nums, 0, path)
        return res

    def findSubsequences1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtracking(nums, startindex, path):
            if len(path)>1:
                res.append(path[:])
            if startindex==len(nums):
                return
            
            for i in range(startindex, len(nums)):
                if path and nums[i]<path[-1]:
                    continue
                if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue
                used[i]=True
                path.append(nums[i])
                backtracking(nums, i+1, path)
                used[i]=False
                path.pop()
        used = [True]*len(nums)
        res, path = [], []
        backtracking(nums, 0, path)
        return res

solution = Solution()
res0 = solution.findSubsequences([1,2,3,4,5,6,7,8,9,10,1,1,1,1,1])
res1 = solution.findSubsequences1([1,2,3,4,5,6,7,8,9,10,1,1,1,1,1])
for _ in res0:
    res1.remove(_)
print(res1)