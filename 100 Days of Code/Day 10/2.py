# 278. First Bad Version (leetcode)
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n: int) -> int:
        # print(n)
        if n == 1:
            return n
        else:
            first = 1
            last = n
            while first <= last:
                mid = (first + last) // 2
                x = isBadVersion(mid)

                if x == False:
                    first = mid + 1
                if x == True:
                    if mid == 1:
                        return 1
                    else:
                        y = isBadVersion(mid - 1)
                        if y != True:
                            return mid
                        else:
                            last = mid - 1

        """
        :type n: int
        :rtype: int
        """
