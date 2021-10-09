# 876. Middle of the Linked List (leetcode)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return(head)
        len=0
        curr=head
        while(head):
            len=len+1
            head=head.next
        #print(len)
        x=int(len/2)
        y=0
        while(y!=x):
            curr=curr.next
            y=y+1
        return(curr)