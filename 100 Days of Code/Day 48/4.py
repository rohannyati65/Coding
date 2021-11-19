# 461. Hamming Distance (leetcode)
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        if x > y:
            x, y = y, x
        a = str(bin(x))
        a = a[2:]
        b = str(bin(y))
        b = b[2:]
        # print(a,b)
        a = "0" * (len(b) - len(a)) + a
        # print(a,b)
        count = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1
        return count
