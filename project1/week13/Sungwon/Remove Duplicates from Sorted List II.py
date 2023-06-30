class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        answer = tail = ListNode()
        while head:
            print(head.val)
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
            else:
                tail.next = head
                tail = tail.next
            head = head.next
        tail.next = None
        return answer.next
