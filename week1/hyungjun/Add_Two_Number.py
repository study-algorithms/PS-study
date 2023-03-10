# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        ret = ListNode()
        _ret = ret
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            if l1_val + l2_val + carry >= 10:
                ret.val = (l1_val+l2_val+carry-10)
                carry = 1
            else:
                ret.val = (l1_val+l2_val+carry)
                carry = 0
            l1, l2 = l1.next if l1 else l1, l2.next if l2 else l2
            ret.next = ListNode() if (l1 or l2 or carry) else None
            ret = ret.next
        return _ret
