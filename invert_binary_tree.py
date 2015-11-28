# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return
        else:
            temp1=root.left
            temp2=root.right
            root.left=temp2
            root.right=temp1
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root