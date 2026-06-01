# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0
        counter = 0

        curr = head

        while (curr):
            length += 1
            curr = curr.next

        #print(length)

        # removing the head
        if length == n:
            head = head.next
        
        curr = head
        while (curr):
            counter += 1
            if (length - counter) == (n):
                #print(counter, curr.val)
                curr.next = curr.next.next
            
            curr = curr.next

        return head
            