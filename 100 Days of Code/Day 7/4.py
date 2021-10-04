# 147. Insertion Sort List (leetcode)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        while head:
            l.append(head.val)
            head = head.next

        l.sort()
        h = ListNode()
        ans = h
        for i in l:
            a = ListNode(i)
            h.next = a
            h = h.next
        return ans.next
