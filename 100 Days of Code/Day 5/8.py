# 143. Reorder List (leetcode)

# 1st attempt
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        p = head
        c = 0
        while p:
            p = p.next
            c += 1

        if c < 3:
            return head

        l = head
        r = head
        p = head
        for i in range(c // 2):
            t = l.next
            while r.next:
                if p.next.next == None:
                    r = r.next
                    p.next = None

                else:
                    r = r.next
                    p = p.next
            l.next = r
            r.next = t
            if (t.next == None) or (t.next.next == None):
                return head
            l = t
            r = l
            p = l

        """
        Do not return anything, modify head in-place instead.
        """


# 2nd attempt
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        p = head
        c = 0
        l = []
        while p:
            l.append(p.val)
            p = p.next
            c += 1

        if c < 3:
            return head

        a = c // 2
        x = l[:a]
        y = l[a:]
        # print(x,y)
        y = y[::-1]

        if len(l) % 2 == 0:
            fast = head.next
            for i in range(len(y)):
                f = ListNode(y[i])
                head.next = f
                if i == (len(y) - 1):
                    head = head.next
                    head.next = None
                else:
                    f.next = fast
                    head = head.next.next
                    fast = fast.next

        else:
            if len(y) == 1:
                fast = head.next
                f = ListNode(y[i])
                head.next = f
                f.next = fast
                head.next.next = None

            else:
                fast = head.next
                for i in range(len(y)):
                    f = ListNode(y[i])
                    head.next = f
                    if i == (len(y) - 1):
                        head.next = None
                    else:
                        f.next = fast
                        head = head.next.next
                        fast = fast.next
