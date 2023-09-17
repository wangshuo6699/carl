class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        i = 1
        result = 0
        intervals = sorted(intervals, key=lambda x: x[0])
        while i<len(intervals):
            if intervals[i][0]<intervals[i-1][1]:
                result += 1
                intervals[i][1] = min(intervals[i-1][1], intervals[i][1])
            i+=1
        return result

solution = Solution()
res = solution.eraseOverlapIntervals(intervals=[[1,2],[1,2],[1,2]])
print(res)
