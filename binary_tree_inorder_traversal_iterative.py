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
        stack=[]
        (stack,root)=self.pushall(stack,root)
        while stack!=[]:
            root=stack.pop()
            result.append(root.val)
            if root.right is not None:
                root=root.right
                (stack,root)=self.pushall(stack,root)
        return result
        
    def pushall(self,stack,root):
            while root is not None:
                stack.append(root)
                if root.left is not None:
                    root=root.left
                else:
                    break
            return (stack, root)
