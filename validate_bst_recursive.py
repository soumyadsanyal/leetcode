# Definition for a binary tree node.
 class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def isValidBST(self, root, leftguard=None, rightguard=None):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if leftguard is None and rightguard is None:
            return self.isValidBST(root.left,leftguard=leftguard,rightguard=root.val) and self.isValidBST(root.right,leftguard=root.val,rightguard=rightguard)
        if leftguard is None:
            return root.val < rightguard and self.isValidBST(root.left,leftguard=leftguard,rightguard=root.val) and self.isValidBST(root.right,leftguard=root.val,rightguard=rightguard)
        if rightguard is None:
            return leftguard < root.val and self.isValidBST(root.left,leftguard=leftguard,rightguard=root.val) and self.isValidBST(root.right,leftguard=root.val,rightguard=rightguard)
        else:
            return leftguard < root.val < rightguard and self.isValidBST(root.left,leftguard=leftguard,rightguard=root.val) and self.isValidBST(root.right,leftguard=root.val,rightguard=rightguard)
            