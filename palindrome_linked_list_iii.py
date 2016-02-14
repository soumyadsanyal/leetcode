# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        if head.next is None:
            return True
        start=head
        head.prev=None
        while True:
            temp=head
            head=head.next
            head.prev=temp
            if head.next is None:
                break
        return self.pred(start, head)
 
        
    def pred(self, n1, n2):
        if n1 is None and n2 is None:
            return True
        else:
            return n1.val==n2.val and self.pred(n1.next, n2.prev)