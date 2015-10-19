# Definition for singly-linked list.
 class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.R(None, head)
        
    
    
    
    
    def R(self,f,s):
        if s is None:
            return f
        else:
            temp=s.next
            s.next=f
            return self.R(s,temp)