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

        def backtracking(i):
            if i == len(digits):
                combinations.append(''.join(combination))
                return
            else:
                digit = digits[i]
                for letter in digit_map[digit]:
                    combination.append(letter)
                    backtracking(i+1)
                    combination.pop()
        combination, combinations = [], []
        backtracking(0)
        return combinations

solution = Solution()
print(solution.letterCombinations("2"))
