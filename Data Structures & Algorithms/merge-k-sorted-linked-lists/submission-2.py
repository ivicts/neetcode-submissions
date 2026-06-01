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

        counter = 0

        while (len(lists) > 1):
            res = []

            for i in range(0, len(lists), 2):
                firstList = lists[i]
                secondList = lists[i + 1] if (i + 1) < len(lists) else None
                res.append(self.mergeList(firstList, secondList))
            lists = res
            # if counter < 5:
            #     print(len(lists))
            # counter += 1

        return lists[0]



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