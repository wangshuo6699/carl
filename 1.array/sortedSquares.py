class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        left, right = 0, len(nums)-1
        while left<=right:
            left_square = nums[left]**2
            right_square = nums[right]**2
            if left_square>right_square:
                res.insert(0, left_square)
                left += 1
            elif left_square<right_square:
                res.insert(0, right_square)
                right -= 1
            else:
                if left!=right:
                    res.insert(0, left_square)
                    res.insert(0, right_square)
                else:
                    res.insert(0, left_square)
                left += 1
                right -= 1
        return res

solution = Solution()
solution.sortedSquares([-10000,-9999,-7,-5,0,0,10000])
