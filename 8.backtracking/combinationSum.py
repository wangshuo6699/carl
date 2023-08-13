class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtracking(candidates, begin, size, path, res, target):
            if target<0:
                return 
            elif target==0:
                res.append(path)
                return
            for index in range(begin, size):
                backtracking(candidates, index, size, path+[candidates[index]], res, target-candidates[index])
        size = len(candidates)
        res, path = [], []
        backtracking(candidates, 0, size, path, res, target)
        return res

solution = Solution()
print(solution.combinationSum([2,3,6,7], 7))
