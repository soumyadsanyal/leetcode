# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def nokids(self,root):
        if root.left is None and root.right is None:
            return 0
        if root.left is None or root.right is None:
            return 1
        else:
            return 2
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if self.nokids(root)==2:
            return 1+min(self.minDepth(root.left),self.minDepth(root.right))
        if self.nokids(root)==1:
            return 1+max(self.minDepth(root.left),self.minDepth(root.right))
        else:
            return 1
            