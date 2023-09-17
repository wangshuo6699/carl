class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key=lambda x: x[0])
        i = 1
        result = []
        while i < len(intervals):
            if intervals[i][0]<intervals[i-1][1]:
                intervals[i][0] = min(intervals[i-1][0], intervals[i][0])
                intervals[i][1] = max(intervals[i-1][1], intervals[i][1])
            else:
                result.append(intervals[i-1])
            i += 1
        result.append(intervals[-1])
        return result

solution = Solution()
res = solution.merge([[1,3],[2,6],[8,10],[15,18]])
print(res)
