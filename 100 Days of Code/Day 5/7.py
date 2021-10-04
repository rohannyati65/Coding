# 92. Reverse Linked List II (leetcode)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        l = []
        while head:
            l.append(head.val)
            head = head.next

        if len(l) <= 1:
            e = l

        else:
            a = left - 1
            b = right - 1
            c = l[a : b + 1]
            d = c[::-1]
            e = l[:a] + d + l[b + 1 :]

        h = ListNode()
        ans = h
        for i in e:
            f = ListNode(i)
            h.next = f
            h = h.next
        return ans.next
