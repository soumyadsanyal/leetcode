# Definition for a binary tree node.
 class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result=[]
        self.recursive_on_tree(root,result)
        return result
            
    def recursive_on_tree(self,root,result):
        if root is None:
            return
        else:
            self.recursive_on_tree(root.left,result)
            result.append(root.val)
            self.recursive_on_tree(root.right,result)
        return result