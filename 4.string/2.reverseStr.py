class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        for i in range(0, len(s), 2*k):
            if len(s)-i <= k:
                left, right = i, len(s)-1
                while left <= right:
                    s[left], s[right] = s[right], s[left]
                    left += 1
                    right -= 1
            elif len(s)-i <= 2*k:
                left, right = i, i+k-1
                while left <= right:
                    s[left], s[right] = s[right], s[left]
                    left += 1
                    right -= 1
            else:
                j = i + k
                left, right = i, j-1
                while left <= right:
                    s[left], s[right] = s[right], s[left]
                    left += 1
                    right -= 1
        return ''.join(s) 

solution = Solution()
res = solution.reverseStr(s = "abcdefg", k = 2)
print(res)
