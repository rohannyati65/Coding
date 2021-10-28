# 869. Reordered Power of 2 (leetcode)
# 1st Attempt (TLE)
import itertools


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def power(x):
            while x >= 1:
                if x == 1:
                    return True
                x = x / 2
            return False

        l = [str(i) for i in str(n)]
        lst = list(map(list, itertools.permutations(l)))
        for i in lst:
            if i[0] == "0":
                pass
            else:
                y = ""
                for j in i:
                    y = y + j
                y = int(y)
                z = power(y)
                if z == True:
                    return True
                else:
                    pass
        return False


# 2nd Attempt (Correct)
import itertools


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        l = [str(i) for i in str(n)]
        lst = list(map(list, itertools.permutations(l)))
        for i in lst:
            if i[0] == "0":
                pass
            else:
                y = ""
                for j in i:
                    y = y + j
                y = int(y)
                if y > 0 and bin(y).count("1") == 1:
                    return True
                else:
                    pass
        return False
