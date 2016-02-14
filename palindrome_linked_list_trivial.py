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
        a=[]
        b=[]
        while head is not None:
            a.append(head.val)
            b.append(head.val)
            head=head.next
        b.reverse()
        return a==b