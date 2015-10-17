# Definition for singly-linked list.
 class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2, carry=0, head=None):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            if carry==1:
                l1=ListNode(0)
                l2=ListNode(0)
                l3=self.addTwoNumbers(l1,l2,carry=carry,head=head)
            else:
                return
        if l1 is None:
            l1=ListNode(0)
            l3=self.addTwoNumbers(l1,l2,carry=carry,head=head)
        if l2 is None:
            l2=ListNode(0)
            l3=self.addTwoNumbers(l1,l2,carry=carry,head=head)
        if head is not None:
            print(head.val)
        else:
            print(head)
        temp=l1.val+l2.val+carry
        here=temp%10
        carry=int(temp>here)
        l3=ListNode(here)
        if head is None:
            head=l3
        l3.next=self.addTwoNumbers(l1.next,l2.next,carry=carry, head=head)
        return l3 
        