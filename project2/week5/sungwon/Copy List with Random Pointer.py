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
        if head is None:
            return None 
        dictionary = dict()
        curr = head
        while curr:
            dictionary[curr] = Node(curr.val, None, None)
            curr = curr.next
        
        curr = head
        while curr:
            if curr.next:
                dictionary[curr].next = dictionary[curr.next]
            if curr.random:
                dictionary[curr].random = dictionary[curr.random]
            curr = curr.next
        return dictionary[head]
