# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pos = 0
        l1_sum = 0
        while l1:
            l1_sum += l1.val *(10 ** pos)
            l1= l1.next
            pos+=1
      
        pos = 0
        l2_sum = 0
        while l2:
            l2_sum += l2.val *(10 ** pos)
            l2= l2.next
            pos+=1

        res = l1_sum+ l2_sum
        st_res = str(res)

        start, linked = None, None
        for i in st_res:
            if not start:
                start = ListNode(int(i))
                linked = start
            else:
                next_node = ListNode(int(i), linked)
                linked = next_node
        return linked

        

