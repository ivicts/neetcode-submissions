# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = node = ListNode()

        curr1 = list1
        curr2 = list2
        #counter = 0

        while (curr1 and curr2):
            # if counter < 5:
            #     #print(curr1.val, curr2.val)
            #     counter+= 1
            if  curr2.val < curr1.val:
                node.next = curr2
                node = curr2
                curr2 = curr2.next
            elif curr1.val <= curr2.val:
                node.next = curr1
                node = curr1
                curr1 = curr1.next
        
        if curr1:
            node.next = curr1
        else:
            node.next = curr2

        return dummy.next