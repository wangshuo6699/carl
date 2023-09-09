# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        if len(nums)==1:
            return TreeNode(nums[0])
        max_val, max_idx = -float('inf'), 0
        for i in range(len(nums)):
            if nums[i]>max_val:
                max_idx = i
                max_val = nums[i]
        root = TreeNode(max_val)
        # if max_idx>0:
        #     root.left = self.constructMaximumBinaryTree(nums[:max_idx])
        # if max_idx<len(nums)-1:
        #     root.right = self.constructMaximumBinaryTree(nums[max_idx+1:])
        root.left = self.constructMaximumBinaryTree(nums[:max_idx])
        root.right = self.constructMaximumBinaryTree(nums[max_idx+1:])
        return root

solution = Solution()
solution.constructMaximumBinaryTree(nums=[3,2,1,6,0,5])
