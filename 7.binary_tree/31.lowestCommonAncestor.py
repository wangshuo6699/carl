# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 递归法
        # if not root:
        #     return None
        # if root.val>=p and root.val<=q or root.val<=p and root.val>=q:
        #     return root
        # left = self.lowestCommonAncestor(root.left, p, q)
        # if left:
        #     return left
        # right = self.lowestCommonAncestor(root.right, p, q)
        # if right:
        #     return right
        # return False

        # 迭代法
        if not root:
            return False
        while root:
            if root.val>p.val and root.val>q.val:
                self.lowestCommonAncestor(root.left)
            elif root.val<p.val and root.val<q.val:
                self.lowestCommonAncestor(root.right)
            else:
                return root
        return False
            
    
node0 = TreeNode(0)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)

node4.left = node3
node4.right = node5
node2.left = node0
node2.right = node4
node8.left = node7
node8.right = node9
node6.left = node2
node6.right = node8

solution = Solution()
res = solution.lowestCommonAncestor(node6, p=2, q=4)
print(res.val)
