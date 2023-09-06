# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from collections import deque

        if not root:
            return []
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if _==0:
                    result = cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return result


node1 = TreeNode(1)
node3 = TreeNode(3)
root  = TreeNode(2, node1, node3)

solution = Solution()
res = solution.findBottomLeftValue(root)
print(res)
