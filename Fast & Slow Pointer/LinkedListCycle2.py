#Leetcode 142. Linked List Cycle II

from pyparsing import Optional
from LinkListCycle import ListNode

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        flag=True

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                flag=False
                break

        if flag :
            return None

        slow=head

        while slow!=fast:
            slow=slow.next
            fast=fast.next
        
        return slow
