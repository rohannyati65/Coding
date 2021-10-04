# 1669. Merge In Between Linked Lists  (leetcode)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        l1 = []
        while list1:
            l1.append(list1.val)
            list1 = list1.next

        l2 = []
        while list2:
            l2.append(list2.val)
            list2 = list2.next
        l = []
        l = l + l1[:a] + l2 + l1[b + 1 :]
        h = ListNode()
        ans = h
        for i in l:
            a = ListNode(i)
            h.next = a
            h = h.next
        return ans.next
