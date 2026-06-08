# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        #if p and q:
        stack =[[p, q]]
        # elif not p and not q:
        #     return True
        # else:
        #     return False
            

        while stack:

            nodep, nodeq  = stack.pop()
            #print(nodep.val, nodeq.val)

            if not nodep and not nodeq:
                continue

            if (not nodeq) or (not nodep) or (nodep.val != nodeq.val):
                return False

            # if (nodep.left.val != nodeq.left.val) or (nodep.right.val != nodep.right.val):
            #     return False

            #if nodep.left and nodeq.left:
            stack.append([nodep.left, nodeq.left])

            #if nodep.right and nodeq.right:
            stack.append([nodep.right, nodeq.right])



        return True