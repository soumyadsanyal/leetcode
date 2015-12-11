# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def thesort(self,thelist):
        n=len(thelist)
        first, second =thelist[:n//2], thelist[n//2:]
        

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        stack=[]
        if head is None:
            return head
        while head is not None:
            stack.append(head.val)
            head=head.next
        stack.sort()
        stack.reverse()
        temp=stack.pop()
        lag=ListNode(temp)
        start=lag
        while stack!=[]:
            current=ListNode(stack.pop())
            lag.next=current
            lag=lag.next
            current=lag
        return start
            
            #this problem is silly unless you actually implement merge sort yourself!
            
            