# 784. Letter Case Permutation (leetcode)
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        l = [s]
        for i in range(len(s)):
            # print(s[i])
            if (s[i].isalpha()) == True:
                l1 = []
                if s[i].islower() == True:
                    for j in l:
                        if i == 0:
                            l1.append(str(s[i].upper() + j[i + 1 :]))

                        elif i == (len(s) - 1):
                            l1.append(str(j[:i] + s[i].upper()))

                        else:
                            l1.append(str(j[:i] + s[i].upper() + j[i + 1 :]))

                if s[i].isupper() == True:
                    for j in l:
                        if i == 0:
                            l1.append(str(s[i].lower() + j[i + 1 :]))

                        elif i == (len(s) - 1):
                            l1.append(str(j[:i] + s[i].lower()))

                        else:
                            l1.append(str(j[:i] + s[i].lower() + j[i + 1 :]))
                l = l + l1
                # print(l)
        return l
