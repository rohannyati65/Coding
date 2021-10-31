# 5915. Find the Minimum and Maximum Number of Nodes Between Critical Points (leetcode)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        l = []
        while head:
            x = head.val
            l.append(x)
            head = head.next

        l1 = []

        if len(l) < 3:
            return [-1, -1]

        for i in range(1, len(l) - 1):
            if l[i] > l[i - 1] and l[i] > l[i + 1]:
                l1.append(i)

            if l[i] < l[i - 1] and l[i] < l[i + 1]:
                l1.append(i)

        # print(l1)

        if len(l1) < 2 and len(l1) < 2:
            return [-1, -1]

        if len(l1) == 2 and len(l1) == 2:
            return [(l1[1] - l1[0]), (l1[-1] - l1[0])]

        if len(l1) == 2 and len(l1) < 2:
            return [-1, (l1[-1] - l1[0])]

        if len(l1) < 2 and len(l1) == 2:
            return [(l1[1] - l1[0]), -1]

        a = l1[-1] - l1[0]
        b = l1[1] - l1[0]
        for i in range(1, len(l1)):
            # print(i)
            # print(l1[i]-l1[i-1])
            b = min(b, l1[i] - l1[i - 1])

        return [b, a]
