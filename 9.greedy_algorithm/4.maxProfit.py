class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lirun = [prices[i+1]-prices[i] for i in range(len(prices)-1)]
        return sum([_ for _ in lirun if _>0])

solution = Solution()
res = solution.maxProfit(prices=[7,1,5,3,6,4])
print(res)
