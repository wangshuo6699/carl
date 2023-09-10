# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if not root.left and not root.right:
            if val>root.val:
                root.right = val
            else:
                root.left = val
        if val<root.val:
            self.insertIntoBST(root.left, val)
        elif val>root.val:
            self.insertIntoBST(root.right, val)
        return root
        
node1 = TreeNode(1)
node2 = TreeNode(3)
node3 = TreeNode(2, node1, node2)
node4 = TreeNode(7)
node5 = TreeNode(4, node3, node4)

solution = Solution()
solution.insertIntoBST(node5, 5)
