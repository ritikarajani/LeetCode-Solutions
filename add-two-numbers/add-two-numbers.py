# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummyHead = ListNode(0)
        carry = 0
        current = dummyHead
        
        while l1 or l2:
            if l1:
                l1_val = l1.val
            else:
                l1_val = 0
            if l2:
                l2_val = l2.val
            else:
                l2_val = 0
            
            sum = l1_val + l2_val + carry
            
            current.next = ListNode(sum % 10)
            current = current.next
            carry = sum// 10
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry:
            current.next = ListNode(carry)
        
        return dummyHead.next