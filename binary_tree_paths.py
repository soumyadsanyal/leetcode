# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def __init__(self):
        self.results=[]
        self.stack=[]
        
    def binaryTreePaths(self, root):
        self.stack.append(root)
        while self.stack!=[] and root is not None:
            current=self.stack.pop()
            if current.left is not None:
                thenext=current.left
                current.left=None
                self.stack.append(current)
                self.stack.append(thenext)
                continue
            if current.right is not None:
                thenext=current.right
                current.right=None
                self.stack.append(current)
                self.stack.append(thenext)
                continue
            else:
                self.stack.append(current)
                self.results.append("->".join([str(x.val) for x in self.stack]))
                #wrote results to list
                #now rewind till we find a node with a child not visited
                while self.stack!=[]:
                    last=self.stack.pop()
                    if last.left is None and last.right is None:
                        continue
                    else:
                        self.stack.append(last)
                        break
        return self.results
                
                
                
                
