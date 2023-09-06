# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left_num = self.countNodes(root.left)
        right_num = self.countNodes(root.right)
        return left_num+right_num+1

node1 = TreeNode(4)
node2 = TreeNode(5)
node3 = TreeNode(6)
node4 = TreeNode(2, node1, node2)
node5 = TreeNode(3, node3)
root  = TreeNode(1, node4, node5)

solution = Solution()
res = solution.countNodes(root)
print(res)
