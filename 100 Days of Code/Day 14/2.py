# 19. Remove Nth Node From End of List (leetcode)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ans = ListNode(0)
        ans.next = head

        f = ans
        s = ans

        for i in range(1, n + 2):
            f = f.next

        while f is not None:
            f = f.next
            s = s.next

        s.next = s.next.next
        return ans.next
