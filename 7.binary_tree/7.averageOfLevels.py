# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
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
            result.append(sum(level)/len(level))
        return result

        
node9 = TreeNode(9)
node7 = TreeNode(7)
node15 = TreeNode(15)
node20 = TreeNode(20, node15, node7)
node3 = TreeNode(3, node9, node20)

solution = Solution()
res = solution.averageOfLevels(node3)
print(res)
