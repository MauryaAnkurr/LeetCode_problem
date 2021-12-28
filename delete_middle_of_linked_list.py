#Delete the Middle Node of a Linked List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head.next is None:
            return None
        slow_previous =head
        slow = head
        fast =head
        
        while fast and fast.next:
            slow_previous = slow
            slow  =slow.next
            fast =fast.next.next
            
            
        slow_previous.next = slow.next
        
        return head
