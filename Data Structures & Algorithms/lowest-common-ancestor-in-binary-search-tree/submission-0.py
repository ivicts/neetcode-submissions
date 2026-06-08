# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        if p.val < q.val:
            smaller = p
            bigger = q
        else:
            smaller = q
            bigger = p

        if (smaller.val <= root.val) and (root.val <= bigger.val):
            return root

        elif (smaller.val <= root.val) and (bigger.val <= root.val):
            return self.lowestCommonAncestor(root.left, smaller, bigger)
        
        elif (root.val <= smaller.val) and (root.val <= bigger.val):
            return self.lowestCommonAncestor(root.right, smaller, bigger)