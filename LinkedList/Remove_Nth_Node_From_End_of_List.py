# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # we will move right n times
        while n>0 and right:
            right = right.next
            n -= 1
        
        # move both pointers untill right becomes None
        while right:
            left = left.next
            right = right.next
        
        # delete
        left.next = left.next.next
        return dummy.next
        
        
        