# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        if root is None:
            return True
        def isMirror(p,q):
            if not p and not q:  #if both are none
                return True
            if not p or not q:  #if one is none
                return False
            if p.val != q.val:  #if values are unequal
                return False
            return isMirror(p.left,q.right) and isMirror(p.right,q.left)
        
        return isMirror(root.left,root.right)