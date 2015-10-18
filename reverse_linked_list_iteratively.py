# Definition for singly-linked list.
 class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        stack=[]
        root=head
        while root is not None:
            stack.append(root)
            root=root.next
        head=stack.pop()
        temp=head
        while stack != []:
            temp.next=stack.pop()
            temp=temp.next
        temp.next = None
        return head