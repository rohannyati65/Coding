# 5886. Remove Colored Pieces if Both Neighbors are the Same Color (leetcode)
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        if len(colors) < 3:
            return False
        a = 0
        b = 0
        for i in range(0, len(colors) - 2):
            if colors[i] == "A" and colors[i + 1] == "A" and colors[i + 2] == "A":
                a = a + 1

            if colors[i] == "B" and colors[i + 1] == "B" and colors[i + 2] == "B":
                b = b + 1
        # print(a,b)
        if b >= a:
            return False

        if a > b:
            return True
