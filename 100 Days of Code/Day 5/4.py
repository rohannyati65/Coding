# 23. Merge k Sorted Lists (leetcode)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = []
        for i in lists:
            l1 = []
            while i:
                l1.append(i.val)
                i = i.next
            l.append(l1)
        # print(l)
        l2 = []
        for i in l:
            l2 = l2 + i
        l2.sort()
        h = ListNode()
        ans = h
        for i in l2:
            a = ListNode(i)
            h.next = a
            h = h.next
        return ans.next
