class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def valid(sub_s):
            if len(sub_s)>3:
                return False
            elif not sub_s.isdigit():
                return False
            elif int(sub_s)>255:
                return False
            elif sub_s.startswith('0') and len(sub_s)>1:
                return False
            return True
        
        def backtracking(s, startindex, path):
            if startindex==len(s):
                if len(path)==4:
                    res.append('.'.join(path))
                return
            for i in range(startindex, len(s)):
                if not valid(s[startindex: i+1]):
                    continue
                path.append(s[startindex: i+1])
                backtracking(s, i+1, path)
                path.pop()

        res, path = [], []
        backtracking(s, 0, path)
        return res
    
solution = Solution()
solution.restoreIpAddresses('0000')
