# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = -float("inf")

        def dfs(node):#, maxLocalPath):
            nonlocal maxPath
            if node is None:
                return 0

            left_gain = dfs(node.left)
            right_gain =  dfs(node.right)

            maxLocalPath = node.val + max(0, left_gain, right_gain, left_gain + right_gain)
            maxPath = max(maxPath, maxLocalPath)
            bestBranchPath = max(0, left_gain + node.val, right_gain + node.val, node.val)

            return bestBranchPath

        dfs(root)
        return maxPath