"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        record = dict()
        cur = head
        if not cur:
            return head
        new_list = new = Node(cur.val)
        while cur:    
            record[cur] = new
            cur = cur.next
            if not cur:
                break 
            new.next = Node(cur.val)
            new = new.next

        cur = head
        new = new_list

        while cur:
            if cur.random:
                new.random = record[cur.random]
            cur = cur.next
            new = new.next
        return new_list


a = Solution()
print(a.copyRandomList(head = [[3,null],[3,0],[3,null]]))
#[[3,null],[3,0],[3,null]]
