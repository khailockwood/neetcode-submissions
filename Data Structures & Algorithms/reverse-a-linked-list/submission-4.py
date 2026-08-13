# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #recursion: pass node we just looked at as new head every time, get the .next every time, link that node back to head.
        if head is None:
            return head 

        if not head.next:
            return head
        
        newHead = self.reverseList(head.next) #returns final node in linkedlist (new head of reversed)
        head.next.next = head #going back up the calls, sets the previous node's .next to the current node we are going back up on. (i.e list ends at 4, go back to call with node 3, set node 4's .next to node 3)
        head.next = None #this cuts the previous forward link of our node (Node 3's .next no longer equals 4, we can now set it on the next iteration as we go back up)
        return newHead