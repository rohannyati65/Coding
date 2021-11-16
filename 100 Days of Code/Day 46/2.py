# 2073. Time Needed to Buy Tickets (leetcode)
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        a = tickets[k]
        x = 0
        while a != 0:
            for i in range(len(tickets)):
                if tickets[i] != 0:
                    x = x + 1
                    tickets[i] = tickets[i] - 1
                a = tickets[k]
                if a == 0:
                    return x
            a = tickets[k]
        return x
