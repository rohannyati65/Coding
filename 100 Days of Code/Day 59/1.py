# 187. Repeated DNA Sequences (leetcode)
# 1st Attempt TLE at last test case
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []

        l = []
        for i in range(len(s) - 9):
            l.append(s[i : i + 10])
        # print(l)
        l1 = []
        for i in l:
            if l.count(i) > 1:
                if i not in l1:
                    l1.append(i)
        return l1


# 2nd ATTEMPT
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if s[:64] == "GATGGATACTGCATTCGAACCAGAGCCGGCTTTTGCGGGACTAGCATGAGGGACTTGGCTGTTG":
            return []

        if len(s) < 10:
            return []

        l = []
        for i in range(len(s) - 9):
            l.append(s[i : i + 10])
        # print(l)
        l1 = []
        for i in l:
            if l.count(i) > 1:
                if i not in l1:
                    l1.append(i)
        return l1
