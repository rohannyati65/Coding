# 206. Reverse Linked List (leetcode)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        helper = None
        while head is not None:
            next = head.next
            head.next = helper
            helper = head
            head = next
        return helper

        # pre=ListNode(#head.val)
        # while head:
        #    head=head.next
        #    a=ListNode(head.val)
        #    a.next=pre
        #    pre=a
        # return(pre)
