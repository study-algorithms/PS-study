# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def list2node(l:list):
    for i,v in enumerate(l):
        print(v)
        if i == 0:
            prev_node = ListNode(v)
            if len(l)==1:
                return prev_node
        else:
            temp_node = ListNode(v,prev_node)
            prev_node = temp_node
    return temp_node


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def node2int(node):
            return node.val + 10 * node2int(node.next) if node else 0
        answer_int = node2int(l1) + node2int(l2)
        answer_list = [int(i) for i in str(answer_int)]
        return list2node(answer_list)
