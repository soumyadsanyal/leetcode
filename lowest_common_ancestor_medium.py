        # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.codes=[]
        self.head=None
        
    def initial_segment(self,first,second):
        a=[]
        b=[]
        result=[]
        while first!=[]:
            a.append(first.pop())
        while second!=[]:
            b.append(second.pop())
        if a==[] or b==[]:
            return result
        else:
            t=a.pop()
            s=b.pop()
            while t==s:
                result.append(t)
                if a==[] or b==[]:
                    break
                else:
                    t=a.pop()
                    s=b.pop()
            return result
        
     
    
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if self.head is None:
            self.head=root
        s=[]
        s.append([root,[]])
        while s!=[]:
            temp=s.pop()
            n=temp[0]
            sigma=temp[1]
            if n==p or n==q:
                self.codes.append(sigma)
            if len(self.codes)>=2:
                break
            if n.left is not None:
                s.append([n.left,sigma+[0]])
            if n.right is not None:
                s.append([n.right,sigma+[1]])
        print(self.codes)
        first=self.codes.pop()
        second=self.codes.pop()
        this=self.initial_segment(first,second)
        print(this)
        n=self.head
        reversedthis=[]
        while this!=[]:
            reversedthis.append(this.pop())
        while reversedthis!=[]:
            temp=reversedthis.pop()
            if temp==0:
                n=n.left
            elif temp==1:
                n=n.right
            else:
                raise ValueError("whoa!")
        return n
            
        
        
        
            