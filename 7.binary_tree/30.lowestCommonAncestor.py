# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root.val==p or root.val==q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if not left and right:
            return right
        if left and not right:
            return left
        if not left and not right:
            return False

node1 = TreeNode(7)
node2 = TreeNode(4)
node3 = TreeNode(6)
node4 = TreeNode(2, node1, node2)
node5 = TreeNode(0)
node6 = TreeNode(8)
node7 = TreeNode(5, node3, node4)
node8 = TreeNode(1, node5, node6)
root  = TreeNode(3, node7, node8)

solution = Solution()
res = solution.lowestCommonAncestor(root, p=7, q=6)
print(res.val)
