# 374. Guess Number Higher or Lower (leetcode)
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        first = 1
        last = n
        while first <= last:
            mid = (first + last) // 2
            x = guess(mid)
            if x == 0:
                return mid
            elif x < 0:
                last = mid - 1
            else:
                first = mid + 1
        return -1
