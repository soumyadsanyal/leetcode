# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def rev_list(self, head):
        if not head or not head.next:
            return head
        lag, current, skip = None, head, head.next
        while skip:
            current.next=lag
            lag=current
            current=skip
            skip=skip.next
        current.next=lag
        return current
    
    def split(self, head):
        lag, slow, fast = None, head, head
        while fast.next:
            lag=slow
            slow=slow.next
            fast=fast.next
            if fast.next:
                fast=fast.next
        lag.next=None
        return slow

    def ziplist(self, a, b):
        head=a
        while a.next and b.next:
            na=a.next
            nb=b.next
            a.next=b
            b.next=na
            a=na
            b=nb
        a.next=b
        return

        
        
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        if not head.next:
            return
        pinned=head
        start=head
        middle = self.split(pinned)
        last = self.rev_list(middle)
        self.ziplist(start, last)
        return
        
        
