# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if (not root and not subRoot):
            return True
        if (not root or not subRoot):
            return False

        print(root.val, subRoot.val)

        if (root.val == subRoot.val):
            if self.sameTree(root, subRoot):
                return True

        if root.left:
            return self.isSubtree(root.left, subRoot)

        if root.right:
            return self.isSubtree(root.right, subRoot)

        return False

    def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if (not p and not q):
            return True
        if (not p or not q or (p.val != q.val)):
            return False

        if (p.val == q.val):

            leftSameTree = self.sameTree(p.left, q.left)
            rightSameTree = self.sameTree(p.right, q.right)

            return leftSameTree and rightSameTree
        
        return True
