# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def isin(self, root, p):
        if root is None:
            return False
        elif root==p:
            return True
        else:
            return (self.isin(root.left,p) or self.isin(root.right,p))
            
    def which(self,root,p):
        if root==p:
            return 0
        if self.isin(root.left,p):
            return -1
        else:
            return 1
            
    
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while self.isin(root,p) and self.isin(root,q):
            this=self.which(root,p)
            that=self.which(root,q)
            if this!=that or (this==0 and that==0):
                return root
            else:
                if this==-1:
                    root=root.left
                    continue
                else:
                    root=root.right
                    continue
            