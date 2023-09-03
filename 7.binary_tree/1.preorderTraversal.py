# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 递归法
        # if not root:
        #     return []
        # left = self.preorderTraversal(root.left)
        # right = self.preorderTraversal(root.right)
        # return [root.val]+left+right

        # 迭代法
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

node3 = TreeNode(3)
node2 = TreeNode(2, node3, None)
node1 = TreeNode(1, None, node2)

solution = Solution()
res = solution.preorderTraversal(node1)
print(res)
