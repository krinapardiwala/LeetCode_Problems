# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        node.val=node.next.val  #copy the value of next node into current node
        node.next=node.next.next #skip over to the next node.
        