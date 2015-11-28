# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import Queue

class Solution(object):
    def __init__(self):
        self.s=[]
        self.q=Queue.Queue()
        self.level=0
    
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        if(len(self.s)<self.level+1):
            self.s.append([root.val])
        else:
            self.s[self.level].append(root.val)
        if root.left is not None:
            self.q.put((root.left,self.level+1))
        if root.right is not None:
            self.q.put((root.right,self.level+1))
        if not self.q.empty():
            thenext=self.q.get()
            thenextnode=thenext[0]
            self.level=thenext[1]
            self.levelOrder(thenextnode)
        return self.s
    
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        temp=self.levelOrder(root)
        print(temp)
        temp.reverse()
        return temp
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
    