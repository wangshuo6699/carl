class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        left, right = s[:n], s[n:]
        return right+left

solution = Solution()
res = solution.reverseLeftWords(s="abcdefg", n=2)
print(res)
