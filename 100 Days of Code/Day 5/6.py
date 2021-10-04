# 86. Partition List (leetcode)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l = []
        while head:
            l.append(head.val)
            head = head.next

        l1 = []
        l2 = list(l)
        for i in l:
            if i < x:
                l1.append(i)
                l2.remove(i)
        l1 = l1 + l2
        h = ListNode()
        ans = h
        for i in l1:
            a = ListNode(i)
            h.next = a
            h = h.next
        return ans.next
