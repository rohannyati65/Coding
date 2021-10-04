# 25. Reverse Nodes in k-Group (leetcode)

# 1st attempt

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k < 2:
            return head

        f = head
        p = head
        l = head
        h = head
        count = 0
        while head:
            head = head.next
            count += 1
        if count > k:
            x = count // k
            a = 0
            for i in range(x):
                h = f.next
                f = h.next
                h.next = p
                p = h
                l.next = f

                if a == 0:
                    t = h
                    a = 1

                if i == 0:
                    temp = l
                    l = f
                    h = f
                    p = f

                else:
                    temp.next = h
                    temp = l
                    l = f
                    h = f
                    p = f

            return t


# 2nd attempt

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k < 2:
            return head

        l = []
        count = 0
        while head:
            l.append(head.val)
            head = head.next
            count += 1

        if count <= k:
            l[:] = l[::-1]
            h = ListNode()
            ans = h
            for i in l:
                a = ListNode(i)
                h.next = a
                h = h.next

            return ans.next

        if count > k:
            x = count // k
            l1 = []
            a = 0
            for i in range(x):
                l2 = l[a : a + k]
                l1 = l1 + l2[::-1]
                a = a + k
            l1 = l1 + l[a:]
            h = ListNode()
            ans = h
            for i in l1:
                a = ListNode(i)
                h.next = a
                h = h.next

            return ans.next
