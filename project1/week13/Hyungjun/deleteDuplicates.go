/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicates(head *ListNode) *ListNode {
	root := head
	var prev *ListNode

	for head != nil {
		if head.Next != nil {
			if head.Next.Val == head.Val {
				next := findNext(head.Val, head)
				if next != nil {
					head.Val = next.Val
					head.Next = next.Next
				} else {
					if prev != nil {
						prev.Next = nil
						break
					} else {
						return prev
					}
				}
			} else {
				prev = head
				head = head.Next
			}
		} else {
			break
		}
	}
	return root
}

func findNext(val int, node *ListNode) *ListNode {

	if node.Val != val {
		return node
	} else {
		if node.Next != nil {
			return findNext(val, node.Next)
		} else {
			return nil
		}
	}
}
