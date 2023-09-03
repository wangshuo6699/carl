# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 递归法
        # if not root:
        #     return []
        # left = self.postorderTraversal(root.left)
        # right = self.postorderTraversal(root.right)
        # return left+right+[root.val]

        # 迭代法
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return list(reversed(result))


node3 = TreeNode(3)
node2 = TreeNode(2, node3)
node1 = TreeNode(1, None, node2)

solution = Solution()
res = solution.postorderTraversal(node1)
print(res)
