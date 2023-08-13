class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def valid(sub_s):
            l, r = 0, len(sub_s)-1
            while l<r:
                if sub_s[l]==sub_s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True
        
        def backtracking(s, startindex, path):
            if startindex==len(s):
                res.append(path[:])
                return
            for i in range(startindex, len(s)):
                if not valid(s[startindex:i+1]):
                    continue
                path.append(s[startindex:i+1])
                backtracking(s, i+1, path)
                path.pop()
        res, path = [], []
        backtracking(s, 0, path)
        return res


solution = Solution()
solution.partition("efe")
