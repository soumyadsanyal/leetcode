# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        s=[]
        h={}
        k={}
        if head is None:
            return head
        s.append(head)
        h[head.val]=1
        head=head.next
        while head is not None:
            #print(head.val)
            #print([term.val for term in s])
            if head.val in h:
                #print(h)
                if head.val in k:
                    head=head.next
                    continue
                else:
                    s.pop()
                    k[head.val]=1
                    #print(k)
                    head=head.next
                    continue
            else:
                #print(h)
                s.append(head)
                h[head.val]=1
                head=head.next
        #print([term.val for term in s])
        if s==[]:
            return []
        final=s.pop()
        final.next=None
        s.append(final)
        t=[]
        while s!=[]:
            t.append(s.pop())
        start=t.pop()
        left=start
        left.next=None
        while t!=[]:
            right=t.pop()
            left.next=right
            left=right
        return start