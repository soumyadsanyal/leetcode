# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def __init__(self):
        self.vals=[]
        self.head=None
        
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        self.head=head
        while head is not None:
            if head.next is None:
                break
            if head.next.val==head.val:
                head.next=head.next.next
            else:
                head=head.next
        return self.head