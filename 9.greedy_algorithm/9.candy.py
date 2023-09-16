class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        count = [1]*len(ratings)
        for i in range(len(ratings)-1):
            if ratings[i+1]>ratings[i]:
                count[i+1] = count[i]+1
        for j in range(len(ratings)-1, 0, -1):
            if ratings[j-1]>ratings[j]:
                count[j-1] = max(count[j]+1, count[j-1])
        return sum(count)

solution = Solution()
res = solution.candy([1,3,2,2,1])
print(res)
