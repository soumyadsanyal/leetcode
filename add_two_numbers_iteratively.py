# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry=0
        if l1 is not None or l2 is not None:
            if l1 is None:
                l1=ListNode(0)
            if l2 is None:
                l2=ListNode(0)
            (here,thenextcarry)=self.add_the_digits(l1.val,l2.val,carry)
            head=ListNode(here)
            carry=thenextcarry
#            l1=l1.next
#            l2=l2.next
            l3=head
        while (l1.next is not None or l2.next is not None):
            if l1.next is None:
                l1.next=ListNode(0)
            if l2.next is None:
                l2.next=ListNode(0)
            (here,thenextcarry)=self.add_the_digits(l1.next.val,l2.next.val,carry)
            l3.next=ListNode(here)
            carry=thenextcarry
            l1=l1.next
            l2=l2.next
            l3=l3.next
        if carry==1:
            l3.next=ListNode(carry)
        return head
            
    def add_the_digits(self,this,that,carry):
        temp=this+that+carry
        here=temp%10
        carry=int(temp>here)
        return (here,carry)