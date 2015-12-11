# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def postorderTraversal(self, root, started=None):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        stack=[]
        result=[]
        small=[]
        stack.append(root)
        while stack!=[]:
            temp=stack.pop()
            if temp.left is None and temp.right is None:
                result.append(temp.val)
            else:
                if temp.left is not None:
                    small.append(temp.left)
                    temp.left=None
                if temp.right is not None:
                    small.append(temp.right)
                    temp.right=None
                small.append(temp)
                while small!=[]:
                    stack.append(small.pop())
        return result
            
            