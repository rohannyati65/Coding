# 2074. Reverse Nodes in Even Length Groups (leetcode)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        while head != None:
            l.append(head.val)
            head = head.next
        # print(l)
        a = 0
        k = 1
        while a < len(l):
            if k >= len(l[a:]):
                if len(l[a:]) % 2 == 0:
                    b = l[a:]
                    l[a:] = b[::-1]
                a = len(l)
            else:
                b = l[a : a + k]
                if len(b) % 2 == 0:
                    l[a : a + k] = b[::-1]
                a = a + k
                k = k + 1
        # print(l)
        h = ListNode()
        ans = h
        for i in l:
            a = ListNode(i)
            h.next = a
            h = h.next
        return ans.next
