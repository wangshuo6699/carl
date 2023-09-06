# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValid(root.left, root.right)

    def isValid(self, left, right):
        if not left and right:
            return False
        elif left and not right:
            return False
        elif not left and not right:
            return True
        elif left.val != right.val:
            return False
        isvalid1 = self.isValid(left.left, right.right)
        isvalid2 = self.isValid(left.right, right.left)
        return isvalid1&isvalid2

node1 = TreeNode(3)
node2 = TreeNode(4)
node3 = TreeNode(2, node1, node2)
node4 = TreeNode(2, node2, node1)
root  = TreeNode(1, node3, node4)

solution = Solution()
res = solution.isSymmetric(root)
print(res)
