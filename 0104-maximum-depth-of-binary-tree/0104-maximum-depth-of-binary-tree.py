# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0   #if tree is empty the depth is 0.
        left=self.maxDepth(root.left) #recurssion for left subtree
        right=self.maxDepth(root.right) #recurssion for right subtree

        return max(right,left) + 1 #take the largest depth amongst left and right and add 1 for the current node.
        