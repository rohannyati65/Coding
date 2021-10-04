# 445. Add Two Numbers II (leetcode)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        lst1 = []
        while l1:
            lst1.append(l1.val)
            l1 = l1.next

        lst2 = []
        while l2:
            lst2.append(l2.val)
            l2 = l2.next

        a = ""
        for i in lst1:
            a = a + str(i)

        b = ""
        for i in lst2:
            b = b + str(i)

        c = str(int(a) + int(b))
        l = [i for i in c]
        h = ListNode()
        ans = h
        for i in l:
            x = ListNode(i)
            h.next = x
            h = h.next
        return ans.next
