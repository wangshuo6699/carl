# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        path, result = [], []
        if not root:
            return []
        self.backtracking(root, path, result)
        return result

    def backtracking(self, root, path, result):
        path.append(root.val)
        if not (root.left or root.right):
            result.append('->'.join(map(str, path)))
            return
        if root.left:
            self.backtracking(root.left, path, result)
            path.pop()
        if root.right:
            self.backtracking(root.right, path, result)
            path.pop()

node1 = TreeNode(5)
node2 = TreeNode(2, None, node1)
node3 = TreeNode(3)
root  = TreeNode(1, node2, node3)

solution = Solution()
solution.binaryTreePaths(root)
