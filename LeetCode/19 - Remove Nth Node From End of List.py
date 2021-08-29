# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        currentNode = head
        arr = []
        while currentNode:
            arr.append(currentNode)
            currentNode = currentNode.next
            count += 1
        count -= 1 # normalize
        
        if n > count:
            return head.next
        
        prevNode = arr[-(n + 1)]
        prevNode.next = prevNode.next.next
        return head
        
        
            