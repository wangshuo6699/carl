class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast]!=val:
                nums[slow] = nums[fast]
                slow += 1
        return slow

solution = Solution()
print(solution.removeElement([0,1,2,2,3,0,4,2], 2))
