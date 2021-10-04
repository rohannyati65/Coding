# 1290. Convert Binary Number in a Linked List to Integer (leetcode)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        l = []
        while head:
            l.append(head.val)
            head = head.next

        s = ""
        for i in l:
            s = s + str(i)

        return int(s, 2)
