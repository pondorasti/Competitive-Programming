# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        digit = l1.val + l2.val
        l1.val = digit % 10

        if digit > 9:
            if l1.next is None:
                l1.next = ListNode(1)
            elif l2.next is None:
                l2.next = ListNode(1)
            else:
                l1.next.val += 1

        l1.next = self.addTwoNumbers(l1.next, l2.next)
        return l1
