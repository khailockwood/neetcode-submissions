# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ##can we create a new linked list as we go through the old one,
        ##linking backwards, need to create a new node everytime.
        prev = None
        curr = head
        while curr:
            tempNext = curr.next #get the next node
            curr.next = prev #link current node to node behind it
            prev = curr #prev is now our current node
            curr = tempNext #move curr to the next node
        #go to next node, link it to previous node, move previous node to current node, move current node to next node
        return prev
