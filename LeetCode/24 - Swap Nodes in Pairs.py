# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        nextNode = head.next
        head.next = head.next.next
        nextNode.next = head
        head = nextNode

        head.next.next = self.swapPairs(head.next.next)

        return head
