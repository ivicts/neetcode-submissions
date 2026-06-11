# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        curr = root
        counter = k
        stack = []

        while stack or curr:
            while curr:
                
                #print(curr.val)
                stack.append(curr)
                curr = curr.left
                

            curr = stack.pop()
            
            #print(curr.val, counter)
            counter -= 1

            if counter == 0:
                return curr.val

            

            #if curr:
            curr = curr.right
