# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        dummy = ListNode(0)
        new = dummy
        while (head1 != None or head2 != None):
            if (head2 == None):
                print("Head 2 null, set next to:", head1.val)
                new.next = head1
                head1 = head1.next
                new = new.next
                print ("Now at new node:", new.val)
            elif (head1 == None):
                print("Head 1 null, set next to:", head2.val)
                new.next = head2
                head2 = head2.next
                new = new.next
                print ("Now at new node:", new.val)
            elif (head1.val <= head2.val):
                print("list1 <= list2, set next to:", head1.val)
                new.next = head1
                head1 = head1.next
                new = new.next
                print ("Now at new node:", new.val)
            else:
                print("list2 < list, set next to:", head2.val)
                new.next = head2
                head2 = head2.next
                new = new.next
                print ("Now at new node:", new.val)
        return dummy.next

        