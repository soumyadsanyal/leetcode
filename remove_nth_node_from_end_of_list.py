# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        s=[]
        while head is not None:
            s.append(head)
            head=head.next
        s.append(None)
        t=[]
        counter=0
        while s!=[]:
            temp=s.pop()
            if counter!=n:
                t.append(temp)
            counter+=1
        p=t.pop()
        first=p
        while t!=[]:
            p.next=t.pop()
            p=p.next
        return first