# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# V1
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited = {0}
        node = head

        while node is not None:
            if node in visited:
                return True
            else:
                visited.add(node)

            node = node.next

        return False

# V2 - O(1) Memory
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        tortoise = head
        hare = head
        did_intersect = False
        
        while tortoise is not None and hare is not None:
            tortoise = tortoise.next
            if did_intersect:
                hare = hare.next
            elif hare.next is not None:
                hare = hare.next.next
            else:
                return None
                
            if tortoise == hare and did_intersect is False:
                did_intersect = True
                tortoise = head
            
            if tortoise == hare and did_intersect:
                return tortoise
        
        return None
