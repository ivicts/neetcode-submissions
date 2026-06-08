# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root:
            queue = deque([root])
        else:
            queue = deque()

        res = []

        while queue:
            res_inner = []
            len_q = len(queue)

            for i in range(len_q):

                node = queue.popleft()
                res_inner.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            res.append(res_inner)

        return res