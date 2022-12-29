class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode()
        firstNum = 0
        n = 0
        while l1 != None:
            firstNum += l1.val * 10**n
            l1 = l1.next
            n += 1
        
        secondNum = 0
        n = 0
        while l2 != None:
            secondNum += l2.val * 10**n
            l2 = l2.next
            n += 1
        total = firstNum + secondNum

        NodePtr = ans
        for i in reversed(str(total)):
            NodePtr.next = ListNode()
            NodePtr = NodePtr.next
            NodePtr.val = int(i)

        return ans.next
        
