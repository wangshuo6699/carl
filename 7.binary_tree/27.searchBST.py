# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val==val:
            return root
        if root.val > val:
            result = self.searchBST(root.left, val)
        if root.val < val:
            result = self.searchBST(root.right, val)
        return result

node1 = TreeNode(1)
node2 = TreeNode(3)
node3 = TreeNode(2, node1, node2)
node4 = TreeNode(7)
root  = TreeNode(4, node3, node4)

solution = Solution()
solution.searchBST(root, 2)
        