# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        if len(preorder)==1:
            return root

        for i in range(len(inorder)):
            if inorder[i]==root.val:
                break
        in_left = inorder[:i]
        in_right = inorder[i+1:]
        pre_left = preorder[1:len(in_left)+1]
        pre_right = preorder[len(in_left)+1:]

        root.left = self.buildTree(pre_left, in_left)
        root.right = self.buildTree(pre_right, in_right)
        return root
                

solution = Solution()
solution.buildTree(preorder=[3,9,20,15,7], inorder=[9,3,15,20,7])
