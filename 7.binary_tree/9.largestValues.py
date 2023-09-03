# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        from collections import deque
        result = []
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(max(level))
        return result

node1 = TreeNode(5)
node2 = TreeNode(3)
node3 = TreeNode(9)
node5 = TreeNode(2, None, node3)
node4 = TreeNode(3, left=node1, right=node2)
root = TreeNode(1, node4, node5)

solution = Solution()
res = solution.largestValues(root)
print(res)
