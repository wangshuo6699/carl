class Solution(object):
    def test_2_wei_bag_problem(self, weight, value, bagweight):
        dp = [[0 for i in range(bagweight+1)] for j in range(len(weight))]
        for i in range(len(weight)):
            for j in range(1, bagweight+1):
                if weight[i]>j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]]+value[i])
        return dp[len(weight) - 1][bagweight]


weight = [1, 3, 4]
value = [15, 20, 30]
bagweight = 4

solution = Solution()
result = solution.test_2_wei_bag_problem(weight, value, bagweight)
print(result)
