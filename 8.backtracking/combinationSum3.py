class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def backtracking(k, n, startindex, path):
            if sum(path) > n:
                return
            if len(path) == k:
                if sum(path)==n:
                    res.append(path[:])
                return
            for i in range(startindex, 10-(k-len(path))+1):
                path.append(i)
                backtracking(k, n, i+1, path)
                path.pop()

        path, res = [], []
        backtracking(k, n, 1, path)
        return res

solution = Solution()
print(solution.combinationSum3(3, 9))
