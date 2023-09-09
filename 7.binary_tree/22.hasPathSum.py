# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        path, result = [], []
        self.backtracking(root, path, result)
        return [_ for _ in result if sum(_)==targetSum]
        for _ in result:
            if _==targetSum:
                return True
        return False

    def backtracking(self, root, path, result):
        path.append(root.val)
        if not (root.left or root.right):
            result.append(sum(path))
            return
        if root.left:
            self.backtracking(root.left, path, result)
            path.pop()
        if root.right:
            self.backtracking(root.right, path, result)
            path.pop()

node1 = TreeNode(7)
node2 = TreeNode(2)
node3 = TreeNode(11, node1, node2)
node4 = TreeNode(4, node3)
node5 = TreeNode(1)
node6 = TreeNode(4, None, node5)
node7 = TreeNode(13)
node8 = TreeNode(8, node7, node6)
root  = TreeNode(5, node4, node8)

solution = Solution()
res = solution.hasPathSum(root, 22)
print(res)
