# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.pre_val = 0
        self.traversal(root)
        return root

    def traversal(self, root):
        if not root:
            return None
        self.traversal(root.right)
        root.val += self.pre_val
        self.pre_val = root.val
        self.traversal(root.left)


node1 = TreeNode(0)
node2 = TreeNode(2)
node3 = TreeNode(1, node1, node2)

solution = Solution()
solution.convertBST(node3)
