class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        for p in people:
            result.insert(p[1], p)
        return result

solution = Solution()
solution.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])
