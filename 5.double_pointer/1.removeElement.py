class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i, j = 0, 0
        size = len(nums)
        while j<size:
            if nums[j]!=val:
                nums[i] = nums[j]
                i+=1
            j+=1
        return i

solution = Solution()
res = solution.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2)
print(res)
