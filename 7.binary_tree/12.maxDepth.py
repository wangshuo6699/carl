# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 层序遍历
        # from collections import deque
        # if not root:
        #     return 0
        # depth = 0
        # queue = deque([root])
        # while queue:
        #     depth+=1
        #     for _ in range(len(queue)):
        #         cur = queue.popleft()
        #         if cur.left:
        #             queue.append(cur.left)
        #         if cur.right:
        #             queue.append(cur.right)
        # return depth

        # 后序遍历
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1+max(left_depth, right_depth)

node1 = TreeNode(15)
node2 = TreeNode(7)
node3 = TreeNode(9)
node4 = TreeNode(20, node1, node2)
root  = TreeNode(3, node3, node4)

solution = Solution()
res = solution.maxDepth(root)
print(res)
