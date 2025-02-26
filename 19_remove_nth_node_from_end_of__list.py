# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: 
        sentinel = ListNode(0)
        sentinel.next = head
        #prev: node before the deleted node
        #tail: the (n-1)th next node after the deleted node
        #move prev,curr and tail towards the end. if n = 1, link prev to None. otherwise link prev to curr.next
        prev = sentinel
        curr = head
        tail = head
        for i in range(n-1):
            tail = tail.next
        while tail.next:
            tail = tail.next
            curr = curr.next
            prev = prev.next
        if n == 1:
            prev.next = None
        else:
            prev.next = curr.next
        return sentinel.next

# linked list + marker
# time O(N)
# space O(1)
        
        

        

        