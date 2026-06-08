# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if (p is None and q) or (p and q is None):
            return False

        if (p is None and q is None):
            return True

        if (p.val != q.val):
            return False

        elif (p.val == q.val):
            leftSameTree = self.isSameTree(p.left, q.left)
            rightSameTree = self.isSameTree(p.right, q.right)

            if not leftSameTree or not rightSameTree:
                return False

        return True