# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        first=head
        h1=first
        if first.next is None:
            return first
        else:
            second=first.next
            h2=second
        current=second
        flip=0
        while current.next is not None:
            if flip==0:
                first.next=current.next
                first=first.next
                current=first
                flip=1
            else:
                second.next=current.next
                second=second.next
                current=second
                flip=0
        if flip==0:
            first.next=h2
            second.next
        else:
            second.next=current.next
            first.next=h2
        return h1
        
            
        