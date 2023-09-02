class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for _ in s:
            if not stack:
                stack.append(_)
            elif stack[-1]==_:
                stack.pop()
            else:
                stack.append(_)
        return ''.join(stack)

solution = Solution()
res = solution.removeDuplicates("abbaca")
print(res)
