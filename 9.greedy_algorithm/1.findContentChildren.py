class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        j, result = len(s)-1, 0
        for i in reversed(g):
            while j>=0 and s[j]>=i:
                j -= 1
                result += 1
                break
        return result

solution = Solution()
res = solution.findContentChildren(g=[1,2,3], s=[1,1])
print(res)
