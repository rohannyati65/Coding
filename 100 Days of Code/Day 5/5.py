# 82. Remove Duplicates from Sorted List II (leetcode)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        l1 = []
        for i in l:
            if l.count(i) == 1:
                l1.append(i)
        l1 = list(set(l1))
        l1.sort()
        h = ListNode()
        ans = h
        for i in l1:
            a = ListNode(i)
            h.next = a
            h = h.next
        return ans.next
