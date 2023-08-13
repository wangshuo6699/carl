class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        used = [0]*len(candidates)
        def backtracking(candidates, k, startIndex, path):
            if k<0:
                return
            elif k==0:
                res.append(path[:])
                return
            for i in range(startIndex, len(candidates)):
                if i>0 and candidates[i]==candidates[i-1] and not used[i-1]:
                    continue
                used[i] = True
                path.append(candidates[i])
                backtracking(candidates, k-candidates[i], i+1, path)
                used[i] = False
                path.pop()
        res, path = [], []
        backtracking(candidates, target, 0, path)
        return res

solution = Solution()
solution.combinationSum2([2,5,2,1,2], 5)
            