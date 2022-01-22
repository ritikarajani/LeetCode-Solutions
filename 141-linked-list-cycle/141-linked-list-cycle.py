# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        marker1 = node
        marker2 = node
        
        while marker2 != None and marker2.next != None:
            marker1 = marker1.next
            marker2 = marker2.next.next
            
            if marker1 == marker2 :
                return True
        return False
        