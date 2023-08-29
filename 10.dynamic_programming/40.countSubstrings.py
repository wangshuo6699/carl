class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        dp = [[0]*len(s) for _ in s]
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i]==s[j]:
                    if j-i<2:
                        result+=1
                        dp[i][j]=1
                    else:
                        if dp[i+1][j-1]:
                            result += 1
                            dp[i][j]=1
        return result

solution = Solution()
res = solution.countSubstrings("aaa")
print(res)
