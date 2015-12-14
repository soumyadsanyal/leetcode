# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def isleft(self,inorder,candidate,term):
        if inorder.index(candidate.val)<inorder.index(term.val):
            return True
        else:
            return False
            
    def isright(self,inorder,candidate,term):
        if inorder.index(candidate.val)>inorder.index(term.val):
            return True
        else:
            return False

    
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder==[] or inorder==[]:
            return None
        if len(preorder)==1:
            return TreeNode(preorder[0])
        else:
#           make two stacks: L and R.
            L,R=[],[]
            root=TreeNode(preorder[0])
            L.append(root)
            index=1
            flag="noflag"
            while root.right is None and index<len(preorder):
                #get next candidate from preorder 
                candidate=TreeNode(preorder[index])
                index+=1
                #print("there are %d elements in L"%len(L))
                #print(L,R)
                j=0
                while j<len(L):
                    term=L[j]
                    #print("the candidate is %s"%candidate.val)#,term.val,list(map(lambda x: x.val,L)))
                    #print("the term is %d"%term.val)
                    if self.isleft(inorder,candidate,term):# we know that candidate is in the left subtree:
                        #print("%s is to the left of %s"%(candidate.val,term.val))
                        if term.left is None:
                            term.left=candidate
                            L.append(candidate)
                            #print("appended %s to left of %s"%(candidate.val,term.val))
                            #now process the next candidate from preorder: 
                            break
                        elif term.left is not None: #candidate is in the left subtree, but below this term, so get next term from L:
                         #   print("term %s has left node"%term.val)
                            j=L.index(term.left)
                            continue
                    elif self.isright(inorder,candidate,term):# we know that candidate is in the right subtree:
                        #print("%s is to the right of %s"%(candidate.val,term.val))
                        if term.right is None:
                            term.right=candidate
                            L.append(candidate)
                         #   print("appended candidate to right, L")
                            if term==L[0]:
                                #print("assigned right node to root")
                                root=term
                            #now process the next candidate from preorder: 
                            break
                        elif term.right is not None:
                            j=L.index(term.right)
                            continue# candidate is in the right subtree, but below this term, so get next term from L:
            #at this point, root.right has been assigned, and we have the next (correct) index into preorder. we are done filling L
            #print(list(map(lambda x: x.val,L)))
            R.append(L.pop())
            #from now until we are done processing preorder, we need to populate the right subtree of the tree. it currently holds root.right
            while index<len(preorder):
                #get next candidate from preorder; 
                candidate=TreeNode(preorder[index])
                index+=1
                j=0
                while j<len(R):
                    term=R[j]
                    if self.isleft(inorder,candidate,term):# we know that candidate is in the left subtree of root.right
             #       print("%s is to the left of %s"%(candidate.val,term.val))
                        if term.left is None:
                            term.left=candidate
                            R.append(candidate)
              #          print("appended candidate to left, R")
                        #process the next candidate: 
                            break
                        elif term.left is not None:
                            j=R.index(term.left)
                        #we know that candidate is in the left subtree, but below this node, so get next term
                            continue
                    elif self.isright(inorder,candidate,term):
               #     print("%s is to the right of %s"%(candidate.val,term.val))
                    #we know that the candidate is in the right subtree of root.right
                        if term.right is None:
                            term.right=candidate
                            R.append(candidate)
               #        print("appended candidate to right, R")
                        #process the next candidate: 
                            break
                        elif term.right is not None:
                            j=R.index(term.right)
                        #we know that the candidate is in the right subtree, but below this node, so get next term
                            continue
            #at this point, we have processed all of preorder
            return L[0]
                            
                        
                    
                    