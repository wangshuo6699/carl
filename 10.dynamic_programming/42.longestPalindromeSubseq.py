class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[0]*len(s) for _ in s]
        for i, c in enumerate(s):
            dp[i][i]=1
        for i in range(len(s)-2, -1, -1):
            for j in range(i+1, len(s)):
                if s[i]==s[j]:
                    dp[i][j]=dp[i+1][j-1]+2
                else:
                    dp[i][j]=max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]


solution = Solution()
res = solution.longestPalindromeSubseq("bbbab")
print(res)
