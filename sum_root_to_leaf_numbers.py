# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def __init__(self):
        self.result=[]
    
    def process(self,stack,current):
        thesum=0
        temp=[]
        place=0
        thesum+=(current.val*10**place)
        place+=1
        while stack!=[]:
            thing=stack.pop()
            thesum+=(thing.val*10**place)
            place+=1
            temp.append(thing)
        while temp!=[]:
            stack.append(temp.pop())
        self.result.append(thesum)
        return stack
    
    
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        stack=[]
        v={}
        stack.append(root)
        while stack!=[]:
            current=stack.pop()
            if current not in v:
                if current.left is not None and current.left not in v:
                    stack.append(current)
                    stack.append(current.left)
                elif current.right is not None and current.right not in v:
                    stack.append(current)
                    stack.append(current.right)
                else:
                    v[current]=1
                    if current.left is None and current.right is None:
                        stack=self.process(stack,current)
        return sum(self.result)