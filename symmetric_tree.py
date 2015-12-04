# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def helper(self,this,that):
        if this is None and that is None:
            return True
        if this is None and that is not None:
            return False
        if this is not None and that is None:
            return False
        else:
            return (this.val==that.val) and self.helper(this.left,that.right) and self.helper(this.right,that.left)
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            return self.helper(root.left,root.right)