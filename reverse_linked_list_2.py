# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def reverser(self,node,source,destination):
        if node is None:
            return node
        if node.next is None:
            return node
        s=[]
        while node is not None:
            s.append(node)
            node=node.next
        left=s.pop()
        start=left
        while s!=[]:
            right=s.pop()
            left.next=right
            left=right
        left.next=destination
        source.next=start
        return
    
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m>=n:
            return head
        start=ListNode(0)
        start.next=head
        lag=start
        while m>1:
            lag=lag.next
            head=head.next
            m-=1
            n-=1
        source=lag
        node1=head
        while n>1:
            head=head.next
            n-=1
        destination=head.next
        head.next=None
        self.reverser(node1,source,destination)
        return start.next

