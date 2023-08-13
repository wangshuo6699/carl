import random
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(nums, left, right):
            pivot = nums[left]
            while left < right:
                while left<right and nums[right]>=pivot:
                    right -= 1
                nums[left] = nums[right]

                while left<right and nums[left]<=pivot:
                    left += 1
                nums[right] = nums[left]

            nums[left] = pivot
            return left

        def randomSelect(nums, left, right):
            pivot_index = random.randint(left, right)
            nums[left], nums[pivot_index] = nums[pivot_index], nums[left]
            return partition(nums, left, right)
        
        def quickSort(nums, low, high):
            if low > high:
                return
            # mid = partition(nums, low, high)
            mid = randomSelect(nums, low, high)
            quickSort(nums, low, mid-1)
            quickSort(nums, mid+1, high)

        quickSort(nums, 0, len(nums)-1)
        return nums

solution = Solution()
nums = solution.sortArray([5,1,1,2,0,0])
print()
