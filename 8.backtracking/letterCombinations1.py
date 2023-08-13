class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        if not digits:
            return []
        def backtracking(nums, startindex, path):
            if len(path)==len(digits):
                res.append(''.join(path))
                return
            for char in digit_map[nums[startindex]]:
                path.append(char)
                backtracking(nums, startindex+1, path)
                path.pop()
        
        res, path = [], []
        backtracking(digits, 0, path)
        return res
    
solution = Solution()
solution.letterCombinations("23")
