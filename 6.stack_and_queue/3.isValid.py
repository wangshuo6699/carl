class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        symbol_map = {')': '(', '}': '{', ']': '['}
        for _ in s:
            if _ in symbol_map:
                if not stack:
                    return False
                elif stack[-1]!=symbol_map[_]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(_)
        if stack:
            return False
        return True


solution = Solution()
res = solution.isValid("()")
print(res)
