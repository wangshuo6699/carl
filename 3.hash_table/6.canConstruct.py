from collections import defaultdict

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        char_count = defaultdict(lambda: 0)
        for m in magazine:
            char_count[m] += 1
        for r in ransomNote:
            if r not in char_count:
                return False
            else:
                char_count[r] -= 1
                if char_count[r]<0:
                    return False
        return True

solution = Solution()
res = solution.canConstruct(ransomNote = "aa", magazine = "aab")
print(res)
