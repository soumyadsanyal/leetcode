#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    def getprefix(self,root,p, sigma):
        if root == p or root is None:
            return sigma
        else:
            self.getprefix(root.left,p,sigma.append(0))
            self.getprefix(root.right,p,sigma.append(1))
            
    def getcommoninitialsegment(self,first,second):
        firstprime=[]
        secondprime=[]
        while first!=[]:
            firstprime.append(first.pop())
        while second!=[]:
            secondprime.append(second.pop())
        result=[]
        while True:
            temp1=firstprime.pop()
            temp2=secondprime.pop()
            if temp1==temp2:
                result.append(temp1)
            else:
                break
        return result
        
    
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        first=self.getprefix(root,p,[])
        second=self.getprefix(root,q,[])
        segment=self.getcommoninitialsegment(first,second)
        reversedsegment=[]
        while segment!=[]:
            reversedsegment.append(segment.pop())
        while reversedsegment!=[]:
            temp=reversedsegment.pop()
            if temp==0:
                root=root.left
            if temp==1:
                root=root.right
        return root
        
        
        
        
        
        
        
            
