# 1433. Check If a String Can Break Another String (leetcode)
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        x = string.ascii_lowercase
        y = list(x)
        # print(y)
        s1 = [i for i in s1]
        s2 = [i for i in s2]
        s1.sort()
        s2.sort()
        flag = True
        print(s1, s2)
        for i in range(len(s1)):
            a = y.index(s1[i])
            b = y.index(s2[i])
            print(a, b)
            if a >= b:
                flag = True
                pass
            else:
                flag = False
                break

        if flag == True:
            return True

        for i in range(len(s1)):
            a = y.index(s1[i])
            b = y.index(s2[i])
            print(a, b)
            if b >= a:
                flag = True
                pass
            else:
                flag = False
                break
        return flag
