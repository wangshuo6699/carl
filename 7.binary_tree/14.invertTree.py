# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        # 递归法
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # 迭代法
        stack = [root]
        while stack:
            cur = stack.pop()
            cur.left, cur.right = cur.right, cur.left
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

        return root

node1 = TreeNode(1)
node2 = TreeNode(3)
node3 = TreeNode(6)
node4 = TreeNode(9)
node5 = TreeNode(2, node1, node2)
node6 = TreeNode(7, node3, node4)
root  = TreeNode(4, node5, node6)

solution = Solution()
res = solution.invertTree(root)
print(res)
        