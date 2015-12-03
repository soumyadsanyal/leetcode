# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def __init__(self):
        self.head=None
        
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val<l2.val:
            h=ListNode(l1.val)
            l1=l1.next
        else:
            h=ListNode(l2.val)
            l2=l2.next
        self.head=h
        while (l1 is not None and l2 is not None):
            if l1.val<l2.val:
                h.next=ListNode(l1.val)
                l1=l1.next
                h=h.next
            else:
                h.next=ListNode(l2.val)
                l2=l2.next
                h=h.next
        if l1 is None:
            while l2 is not None:
                h.next=ListNode(l2.val)
                h=h.next
                l2=l2.next
        else:
            while l1 is not None:
                h.next=ListNode(l1.val)
                h=h.next
                l1=l1.next
        h.next=None
        return self.head
        
        
        
        
        
            