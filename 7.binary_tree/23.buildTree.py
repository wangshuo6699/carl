# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder:
            return None

        root = TreeNode(postorder[-1])
        # 叶子节点
        if len(postorder)==1:
            return root

        for i in range(len(inorder)):
            if inorder[i]==root.val:
                break

        in_left = inorder[:i]
        in_right = inorder[i+1:]

        post_left = postorder[:len(in_left)]
        post_right = post_right[len(in_left):-1]
        
        root.left = self.buildTree(in_left, post_left)
        root.right = self.buildTree(in_right, post_right)
        return root

solution = Solution()
solution.buildTree(inorder=[9,3,15,20,7], postorder=[9,15,7,20,3])
