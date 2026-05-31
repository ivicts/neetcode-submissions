# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Find the middle

        slow, fast = head, head.next

        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        #middle = slow
        second = slow.next
        # print("middle ", second.val)
        # print(second.next.val)
        
        #slow.next = None to separate first and second link
        slow.next = None
        prev = None

        # reverse the second linked list

        while (second):
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # the head of the reverse linked list is prev

        first, second = head, prev

        while (second):
           # print(second.val)
            tmp1 = first.next
            tmp2 = second.next
            #print(tmp2)
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2