# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        s=[]
        while head is not None:
            if head.val!=val:
                s.append(head)
            head=head.next
        s.append(None)
        t=[]
        while s!=[]:
            t.append(s.pop())
        p=t.pop()
        first=p
        while p is not None:
            p.next=t.pop()
            p=p.next
        return first
            
            
            