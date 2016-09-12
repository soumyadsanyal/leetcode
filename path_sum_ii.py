# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, thesum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        stack=[]
        results=[]
        stack.append(root)
        while stack!=[] and root is not None:
            current=stack.pop()
            if current.left is not None:
                thenext=current.left
                current.left=None
                stack.append(current)
                stack.append(thenext)
                continue
            if current.right is not None:
                thenext=current.right
                current.right=None
                stack.append(current)
                stack.append(thenext)
                continue
            else:
                #leaf node
                stack.append(current)
                #pushed back on stack, stack now represents a root-leaf path
                #need to check if sum is correct
                localPath=[int(x.val) for x in stack]
                if sum(localPath)==thesum:
                    results.append(localPath)
                    #recorded path if sum matches
                #now rewind stack
                while stack!=[]:
                    last=stack.pop()
                    if last.left is None and last.right is None:
                        continue
                    else:
                        stack.append(last)
                        break
        return results
                
                
                
                
            
