# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head,head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        list2 = slow.next
        slow.next = None
        prev = None
        while list2:
            temp = list2.next
            list2.next = prev
            prev = list2
            list2 = temp
        
        while prev:
            temp1,temp2 = head.next, prev.next
            head.next = prev
            prev.next = temp1
            head,prev = temp1,temp2