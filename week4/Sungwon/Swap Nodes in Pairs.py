class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        index = 0
        answer = head
        prevNode = None

        while head != None and head.next != None:
            if index%2 == 1:
                prevNode = head
            else:
                curNode = head
                nextNode = head.next
                nextNextNode = nextNode.next
                nextNode.next = curNode
                curNode.next = nextNextNode
                if prevNode != None:
                    prevNode.next = nextNode
            index += 1
            print(index, head.val)
            head = head.next
        return answer
