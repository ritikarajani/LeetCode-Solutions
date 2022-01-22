# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return 
        else:
            curr = head
            temp = set([curr.val])
            while curr.next:
                if curr.next.val in temp:
                    curr.next = curr.next.next
                else:
                    temp.add(curr.next.val)
                    curr = curr.next
            return head
        