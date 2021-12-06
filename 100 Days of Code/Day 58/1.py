# 2094. Finding 3-Digit Even Numbers (leetcode)
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        s = set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i != j and i != k and j != k and digits[k] % 2 == 0:
                        val = digits[i] * 100 + digits[j] * 10 + digits[k]
                        if val >= 100:
                            s.add(val)
        return sorted(s)
