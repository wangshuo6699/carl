# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if not root1: return root2
        if not root2: return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1

node1 = TreeNode(5)
node2 = TreeNode(3, node1)
node3 = TreeNode(2)
root1 = TreeNode(1, node2, node3)

node4 = TreeNode(4)
node5 = TreeNode(7)
node6 = TreeNode(1, None, node4)
node7 = TreeNode(3, None, node5)
root2 = TreeNode(2, node6, node7)

solution = Solution()
res = solution.mergeTrees(root1, root2)
print(res)
