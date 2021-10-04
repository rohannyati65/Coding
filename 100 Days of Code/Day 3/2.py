# Split Linked List in Parts (leetcode)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:

        l = []
        curr = head
        while curr:
            l.append(curr.val)
            curr = curr.next
        # print(l)
        l1 = []
        if len(l) < k:
            for i in l:
                l1.append([i])
            a = k - len(l)
            while a != 0:
                a = a - 1
                l1.append([])
            # print(l1)
            lst = []

            for i in l1:
                if len(i) == 0:
                    z = ListNode()
                    lst.append(z.next)
                else:
                    z = ListNode(i[0])
                    lst.append(z)

            return lst

        else:
            l2 = []
            x = len(l) // k
            for i in range(k):
                l2.append(x)
            b = len(l) - (k * x)
            if b != 0:
                for i in range(b):
                    l2[i] = l2[i] + 1

            l1 = []
            a = 0
            for i in l2:
                l1.append(l[a : a + i])
                a = a + i

            lst = []

            h = ListNode()
            ans = h
            for i in l1:
                h = ListNode()
                ans = h
                for j in i:
                    z = ListNode(j)
                    h.next = z
                    h = h.next

                lst.append(ans.next)

            return lst
