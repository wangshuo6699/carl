class Solution(object):
    def test_1_wei_bag_problem(self, weight, value, bagweight):
        dp = [0 for i in range(bagweight+1)]
        dp[0] = 0
        for i in range(len(weight)):
            for j in range(bagweight, -1, -1):
                if j<weight[i]:
                    dp[j] = dp[j]
                else:
                    dp[j] = max(dp[j], dp[j-weight[i]]+value[i])
        return dp[-1]


weight = [1, 3, 4]
value = [15, 20, 30]
bagweight = 4

solution = Solution()
result = solution.test_1_wei_bag_problem(weight, value, bagweight)
print(result)
