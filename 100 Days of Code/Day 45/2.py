# 203. Remove Linked List Elements (leetcode)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = ListNode(0)
        ans = curr
        while head:
            # print(head)
            if head.val == val:
                curr.next = head.next
                head = head.next

            else:
                curr.next = head
                head = head.next
                curr = curr.next
            # print(curr)
        return ans.next
