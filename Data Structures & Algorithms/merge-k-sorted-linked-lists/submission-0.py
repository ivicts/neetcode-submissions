# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # node = dummy = ListNode()
        if len(lists) == 0:
            return 

        for i in range(1, len(lists)):
            newHead = self.mergeList(lists[i], lists[i -1])
            lists[i] = newHead

        return lists[-1]




    def mergeList(self,  first: Optional[ListNode], second: Optional[ListNode]) -> Optional[ListNode]:
        
        node = head = ListNode()

        while (first and second):

            if first.val <= second.val:
                node.next = first
                first = first.next
            else:
                node.next = second
                second = second.next

            node = node.next

        node.next = first if first else second
        
        return head.next