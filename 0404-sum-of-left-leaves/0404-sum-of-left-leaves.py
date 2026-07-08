# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        def isLeaf(node):
            return node and not node.left and not node.right
            #returns true if a node exists and has no children
        total=0
        if isLeaf(root.left):
            total+=root.left.val
        else:
            total+=self.sumOfLeftLeaves(root.left)
        total+=self.sumOfLeftLeaves(root.right)

        return total