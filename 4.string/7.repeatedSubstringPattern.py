class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        next = self.getNext(s)
        if next[-1]!=0 and len(s)%(len(s)-next[-1])==0:
            return True
        return False

    def getNext(self, s):
        j, next = 0, [0]*len(s)
        for i in range(1, len(s)):
            while j>0 and s[i]!=s[j]:
                j = next[j-1]
            if s[i]==s[j]:
                j+=1
            next[i]=j
        return next

solution = Solution()
res = solution.repeatedSubstringPattern("abab")
print(res)
