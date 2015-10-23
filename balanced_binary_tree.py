# Definition for a binary tree node.
 class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None



            
class Solution(object):

    def helper(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return (-1,-1,0,0)
        else:
            l=self.helper(root.left)[2]
            r=self.helper(root.right)[2]
            return [l,r,1+max(l,r),l-r]

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            balance=self.helper(root)[3]
            if balance<-1 or balance>1:
                return False
            else:
                return self.isBalanced(root.left) and self.isBalanced(root.right) 
        
        
        
        