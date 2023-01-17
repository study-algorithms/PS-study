# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # empty or only one
        if not head or not head.next:
            return head
        ret_head = head.next
        prev = None
        while head and head.next:
            tmp = head.next
            head.next = head.next.next
            tmp.next = head
            if prev:
                prev.next = tmp
            prev = head
            head = head.next
        return ret_head
