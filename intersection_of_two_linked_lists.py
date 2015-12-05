# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        result=None
        p=headA
        q=headB
        h={}
        while p is not None:
            h[p.val]=1
            p=p.next
        while q is not None:
            if q.val in h:
                return q
            q=q.next
        return result