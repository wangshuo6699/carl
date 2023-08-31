class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = [_ for _ in s.split() if _]
        left, right = 0, len(s)-1
        while left<right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -=1
        return ' '.join(s)

solution = Solution()
res = solution.reverseWords(s = "the sky is blue")
print(res)
