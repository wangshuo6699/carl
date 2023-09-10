# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def traversal(self, root):
        if not root:
            return []
        left = self.traversal(root.left)
        right = self.traversal(root.right)
        return left+[root.val]+right

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        from collections import Counter
        bt_list = self.traversal(root)
        counter = Counter(bt_list)
        max_freq = max(list(counter.values()))
        result = []
        for k, v in counter.items():
            if v==max_freq:
                result.append(k)
        return result


node1 = TreeNode(2)
node2 = TreeNode(2, node1)
root = TreeNode(1, None, node2)
root = TreeNode(1)

solution = Solution()
res = solution.findMode(root)
print(res)
