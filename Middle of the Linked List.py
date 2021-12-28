#Given the head of a singly linked list, return the middle node of the linked list.

#If there are two middle nodes, return the second middle node.

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow_pointer = head
        fast_pointer = head
        while fast_pointer and fast_pointer.next :
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            
        return slow_pointer
