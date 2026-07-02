# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        curr=head

        while curr:
            if curr.next and curr.val==curr.next.val: #if node is duplicate
                while curr.next and curr.val==curr.next.val: #while nodes are duplicate
                    curr=curr.next  #skip all nodes
                prev.next=curr.next
            else:
                prev=prev.next   #if not duplicate,move the prev pointer
            curr=curr.next  
        return dummy.next
        