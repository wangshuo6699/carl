# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        # 递归法
        # left = self.inorderTraversal(root.left)
        # right = self.inorderTraversal(root.right)
        # return left+[root.val]+right

        # 迭代法
        stack = []
        result = []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                result.append(cur.val)
                cur = cur.right
        return result

# node3 = TreeNode(3)
# node2 = TreeNode(2, node3)
# node1 = TreeNode(1, None, node2)

node1 = TreeNode(1)
node2 = TreeNode(2)
node6 = TreeNode(6)
node4 = TreeNode(4, node1, node2)
node5 = TreeNode(5, node4, node6)

solution = Solution()
res = solution.inorderTraversal(node5)
print(res)
