# 24. Swap Nodes in Pairs  (leetcode)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None) or (head.next is None):
            return head
        prev = head
        head = head.next
        ans = head
        while prev.next:
            t = prev
            prev.next = head.next
            head.next = prev

            if prev.next is None:
                break

            else:
                prev = prev.next
                if prev.next is None:
                    t.next = prev
                else:
                    head = prev.next
                    t.next = head
        return ans
