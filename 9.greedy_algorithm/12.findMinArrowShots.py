class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        i = 0
        result = 1
        points = sorted(points, key=lambda x: x[0])
        while i < len(points):
            if points[i][0]>points[i-1][1]:
                result += 1
            else:
                points[i][1] = min(points[i-1][1], points[i][1])
            i+=1
        return result

solution = Solution()
res = solution.findMinArrowShots(points = [[1,2],[2,3],[3,4],[4,5]])
print(res)
