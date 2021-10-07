# 371. Sum of Two Integers (leetcode)
class Solution:
    def getSum(self, a: int, b: int) -> int:
        m = 0xFFFFFFFF
        while b & m > 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        return (a & m) if b > 0 else a
