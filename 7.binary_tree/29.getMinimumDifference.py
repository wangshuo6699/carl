# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution(object):
#     def traversal(self, root):
#         if not root:
#             return []
#         left = self.traversal(root.left)
#         right = self.traversal(root.right)
#         return left+[root.val]+right

#     def getMinimumDifference(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         self.vec = self.traversal(root)
#         if len(self.vec)<2:
#             return 0
#         min_val = float('inf')
#         for i in range(len(self.vec)-1):
#             min_val = min(min_val, self.vec[i+1]-self.vec[i])
#         return min_val

class Solution(object):
    def __init__(self):
        self.pre = None
        self.min_val = float('inf')

    def traversal(self, root):
        if not root:
            return []
        self.traversal(root.left)
        if self.pre is not None:
            self.min_val = min(self.min_val, root.val-self.pre.val)
        self.pre = root
        self.traversal(root.right) 

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.traversal(root)
        return self.min_val


node1 = TreeNode(2)
node2 = TreeNode(3, node1)
root  = TreeNode(1, None, node2)

solution = Solution()
res = solution.getMinimumDifference(root)
print(res)
