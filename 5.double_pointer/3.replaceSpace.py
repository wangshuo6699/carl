class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for _ in s:
            if _==' ':
                res.append('%20')
            else:
                res.append(_)
        return ''.join(res)

solution = Solution()
res = solution.replaceSpace(s="We are happy.")
print(res)
