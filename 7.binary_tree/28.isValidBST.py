# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self) -> None:
        self.max_val = float('-inf')

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        max_val = -float('inf')
        left = self.isValidBST(root.left)
        if root.val > self.max_val:
            self.max_val = root.val
        else:
            return False
        right = self.isValidBST(root.right)
        return left and right
    #     bt_list = self.inorderTraversal(root)
    #     for i in range(len(bt_list)-1):
    #         if bt_list[i]>=bt_list[i+1]:
    #             return False
    #     return True
    
    # def inorderTraversal(self, root):
    #     if not root:
    #         return []
    #     left = self.inorderTraversal(root.left)
    #     right = self.inorderTraversal(root.right)
    #     return left+[root.val]+right

node1 = TreeNode(1)
node2 = TreeNode(3)
node3 = TreeNode(6)
node4 = TreeNode(4, node2, node3)
root  = TreeNode(5, node1, node4)
# root  = TreeNode(5)

solution = Solution()
res = solution.isValidBST(root)
print(res)
