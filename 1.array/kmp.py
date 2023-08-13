class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0
        p = 0
        next = self.getnext(len(needle), needle)
        for i in range(len(haystack)):
            while p > 0 and needle[p] != haystack[i]:
                p = next[p-1]
            if needle[p] ==  haystack[i]:
                p += 1
            if p == len(needle):
                return i - len(needle) +1
        return -1
    
    def getnext(self, a, needle):
        p = 0
        next = [0]
        for i in range(1, len(needle)):
            while (p>0 and needle[i]!=needle[p]):
                p = next[p-1]
            if needle[i] == needle[p]:
                p += 1
            next.append(p)
        return next

a = Solution()
res = a.strStr('aaaaa', 'bba')
print(res)