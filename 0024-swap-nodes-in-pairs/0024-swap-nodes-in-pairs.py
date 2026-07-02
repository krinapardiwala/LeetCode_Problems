# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy

        while prev.next and prev.next.next:
            first_element=prev.next
            next_element=prev.next.next

            prev.next=next_element
            first_element.next=next_element.next
            next_element.next=first_element

            prev=first_element  #moving forward

        return dummy.next
