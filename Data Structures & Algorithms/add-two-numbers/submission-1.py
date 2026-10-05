# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode()
        head = newList
        carry = 0

        while l1 or l2 or carry == 1:
            if l1:
                val1 = l1.val
            else:
                val1 = 0
            if l2:
                val2 = l2.val
            else:
                val2 = 0

            nodeSum = val1 + val2 + carry

            if nodeSum < 10:
                newNode = ListNode(nodeSum)
                newList.next = newNode
                if l1:
                    l1 = l1.next
                if l2:
                    l2 = l2.next
                carry = 0
            else:
                newNode = ListNode((nodeSum) % 10)
                newList.next = newNode
                if l1:
                    l1 = l1.next
                if l2:
                    l2 = l2.next
                carry = 1
            newList = newList.next
            

        return head.next

            

