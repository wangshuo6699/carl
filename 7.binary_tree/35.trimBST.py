# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        if not root:
            return root
        if root.val<low:
            right = self.trimBST(self.right, low, high)
            return right
        if root.val>high:
            left = self.trimBST(self.left, low, high)
            return left
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root

node1 = TreeNode(0)
node2 = TreeNode(2)
node3 = TreeNode(1, node1, node2)

solution = Solution()
solution.trimBST(node3, 1, 2)
