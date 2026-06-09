# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], lower_bound: float = float('-inf'), upper_bound: float = float('inf')) -> bool:

        if not root:
            return True
        
        if (root.left):
            #if (root.val <= root.left.val) or (upper_bound <= root.left.val) or (root.left.val <= lower_bound):
            if (root.val <= root.left.val) or (upper_bound <= root.left.val) or (root.left.val <= lower_bound):
                return False

        if (root.right):
            if (root.right.val <= root.val) or (upper_bound <= root.right.val) or (root.right.val <= lower_bound):
                return False

        return self.isValidBST(root.left, lower_bound, root.val) and self.isValidBST(root.right, root.val, upper_bound)

            