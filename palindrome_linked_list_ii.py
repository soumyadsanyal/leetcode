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
        start=head
        alt=None
        result=[]
        alts=[]
        while True:
            temp=ListNode(head.val)
            head=head.next
            temp.next=alt
            alt=temp
            if head is None:
                break
        return self.pred(start, alt)
        
    def pred(self, n1, n2):
        if n1 is None and n2 is None:
            return True
        else:
            return n1.val==n2.val and self.pred(n1.next, n2.next)