class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        result = 0
        stack = [0]
        heights.append(0)
        heights.insert(0, 0)
        for i in range(1, len(heights)):
            if heights[i]>heights[stack[-1]]:
                stack.append(i)
            elif heights[i]==heights[stack[-1]]:
                stack.pop()
                stack.append(i)
            else:
                while stack and heights[i]<heights[stack[-1]]:
                    mid = heights[stack[-1]]
                    stack.pop()
                    if stack:
                        left = stack[-1]
                        right = i
                        w = right-left-1
                        result = max(result, w*mid)
                stack.append(i)
        return result

solution = Solution()
res = solution.largestRectangleArea(heights=[2,1,5,6,2,3])
