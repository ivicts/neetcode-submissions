# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        curr = head
        counter = 0
        while (curr):
            curr = curr.next
            if counter > 100:
                return True
            counter += 1

        return False