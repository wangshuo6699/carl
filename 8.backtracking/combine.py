class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backtracking(n, k, startindex, path):
            if len(path)==k:
                res.append(path[:])
                return
            for i in range(startindex, n-(k-len(path))+2):
                path.append(i)
                backtracking(n, k, i+1, path)
                path.pop()
    
        path, res = [], []
        backtracking(n, k, 1, path)
        return res

solution = Solution()
print(solution.combine(4, 2))
