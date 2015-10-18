# Definition for singly-linked list.
 class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        thelength=self.length_list(head)
        k=k%thelength
        if k==0:
            return head
        theposition=thelength-k
        here=self.get_break_point(head,theposition)
        thenext=here.next
        here.next=None
        oldend=self.travel_to_end(thenext)
        oldend.next=head
        return thenext
        
    def travel_to_end(self,head):
        if head is None:
            return head
        current=head
        while current.next is not None:
            current=current.next
        return current
    
    def get_break_point(self,head,distance):
        current=head
        position=1
        while position<distance:
            current=current.next
            position+=1
        return current
        
    
    
    def length_list(self,head):
        length=1
        current=head
        while current.next is not None:
            current=current.next
            length+=1
        return length