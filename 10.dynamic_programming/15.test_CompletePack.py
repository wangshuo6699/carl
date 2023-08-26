class Solution:
    def test_CompletePack(self, weight, value, bagWeight):
        dp = [[0]*(bagWeight+1) for _ in range(len(weight))]
        dp[0][0] = 0
        for i in range(len(weight)):
            for j in range(weight[i], bagWeight+1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-weight[i]]+value[i])
        return dp

if __name__ == "__main__":
    solution = Solution()
    result = solution.test_CompletePack([1, 3, 4], [15, 20, 30], 4)
    print(result)
