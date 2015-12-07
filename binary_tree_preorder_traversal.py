# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        R=[]
        s=[]
        s.append(root)
        while s!=[]:
            temp=s.pop()
            R.append(temp.val)
            if temp.right is not None:
                s.append(temp.right)
            if temp.left is not None:
                s.append(temp.left)
        return R