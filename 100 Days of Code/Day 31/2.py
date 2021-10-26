# 1451. Rearrange Words in a Sentence (leetcode)
class Solution:
    def arrangeWords(self, text: str) -> str:
        l = list(map(str, text.split()))
        l.sort(key=len)
        # print(l)
        x = ""
        for i in range(len(l)):
            if i == 0:
                a = l[0]
                # print(a)
                a = a.replace(a[0], a[0].upper())
                a = a.replace(a[1:], a[1:].lower())
                # print(a)
                x = x + a + " "
                # print(x)

            elif i == (len(l) - 1):
                a = l[i]
                a = a.lower()
                x = x + a

            else:
                a = l[i]
                a = a.lower()
                x = x + a + " "
            # print(x)
        return x
