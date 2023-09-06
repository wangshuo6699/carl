# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not (root.left or root.right):
            return 0
        left_num = self.sumOfLeftLeaves(root.left)
        if root.left and not root.left.left and not root.left.right:
            left_num = root.left.val
        right_num = self.sumOfLeftLeaves(root.right)
        return left_num+right_num

node1 = TreeNode(15)
node2 = TreeNode(7)
node3 = TreeNode(20, node1, node2)
node4 = TreeNode(9)
root  = TreeNode(3, node4, node3)

solution = Solution()
res = solution.sumOfLeftLeaves(root)
print(res)
