class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        hash_map = [0]*26
        for char in s:
            hash_map[ord(char)-ord('a')] += 1
        for char in t:
            hash_map[ord(char)-ord('a')] -= 1
        for num in hash_map:
            if num!=0:
                return False
        return True

solution = Solution()
res = solution.isAnagram(s = "rat", t = "car")
print(res)
