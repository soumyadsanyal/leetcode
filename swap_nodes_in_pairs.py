# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        start=ListNode(0)
        start.next=head
        C=start
        A=head
        B=head.next
        while True:
            #print(A.val,B.val,C.val)
            A.next=B.next
            B.next=A
            C.next=B
            #move two places forward
            try:
                C=A
                A=C.next
                B=A.next
                if B is None:
                    break
            except:
                break
        return start.next