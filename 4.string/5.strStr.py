class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        j = 0
        next = self.getNext(needle)
        for i in range(len(haystack)):
            while j>0 and haystack[i]!=needle[j]:
                j = next[j-1]
            if haystack[i]==needle[j]:
                j += 1
            if j==len(needle):
                return i-len(needle)+1
        return -1
    
    def getNext(self, s):
        j=0
        next = [0]*len(s)
        for i in range(1, len(s)):
            while j>0 and s[i]!=s[j]:
                j = next[j-1]
            if s[i]==s[j]:
                j+=1
                next[i] = j
        return next

solution = Solution()
res = solution.strStr(haystack="sadbutsad", needle="sad")
print(res)
