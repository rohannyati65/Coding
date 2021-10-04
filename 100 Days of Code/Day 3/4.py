# 148. Sort List (leetcode)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        l = []
        while head:
            l.append(head.val)
            head = head.next

        l.sort()

        h = ListNode()
        ans = h
        for i in l:
            f = ListNode(i)
            h.next = f
            h = h.next
        return ans.next
