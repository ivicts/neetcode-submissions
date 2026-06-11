# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        #root = TreeNode(val = preorder[0], left = preorder[1], right = preorder[2])
        preorderIdx = 0
        inOrderMap = {inorder[i]:i for i in range(len(inorder))}


        def dfs(l, r):
            nonlocal preorderIdx
            print(l, r)
            if r >= l and preorderIdx < len(preorder):
                nodeVal = preorder[preorderIdx]
                preorderIdx += 1

                inOrderIdx = inOrderMap[nodeVal]
                node = TreeNode(val= nodeVal, left = dfs(l, inOrderIdx - 1), right = dfs(inOrderIdx + 1, r))
            else:
                node = None
            return node

        
        return dfs(0, len(preorder))