class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for i, num in enumerate(nums):
            if num in hash_map:
                return [hash_map[num], i]
            else:
                hash_map.update({target-num: i})

solution = Solution()
res = solution.twoSum(nums = [2,7,11,15], target = 9)
print(res)
