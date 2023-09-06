# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==[]:
            return True
        if self.getHigh(root)==-1:
            return False
        return True
    
    def getHigh(self, root):
        if not root:
            return 0
        left_high = self.getHigh(root.left)
        right_high = self.getHigh(root.right)
        if left_high==-1 or right_high==-1 or abs(left_high-right_high)>1:
            return -1
        return max(left_high, right_high)+1

node1 = TreeNode(15)
node2 = TreeNode(7)
node3 = TreeNode(20, node1, node2)
node4 = TreeNode(9)
root  = TreeNode(3, node4, node3)

solution = Solution()
res = solution.isBalanced(root)
print(res)
