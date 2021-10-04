# 1721. Swapping Nodes in a Linked List (leetcode)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = []
        while head:
            l.append(head.val)
            head = head.next

        temp = l[k - 1]
        l[k - 1] = l[-k]
        l[-k] = temp

        h = ListNode()
        ans = h
        for i in l:
            a = ListNode(i)
            h.next = a
            h = h.next
        return ans.next
