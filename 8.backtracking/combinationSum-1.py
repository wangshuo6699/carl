class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtracking(n, k, start, path):
            if k < 0:
                return
            elif k==0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                if k < 0:
                    return
                path.append(candidates[i])
                backtracking(n, k-n[i], i, path)
                path.pop()
        
        res, path = [], []
        backtracking(candidates, target, 0, path)
        return res

solution = Solution()
solution.combinationSum([2,3,6,7], 7)
