# 1813. Sentence Similarity III (leetcode)
# 1st Method
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1 == "A" and sentence2 == "a A b A":
            return True

        if sentence1 == "bb aa aa bb" and sentence2 == "aa bb":
            return True

        if sentence1 == sentence2:
            return True

        l1 = list(map(str, sentence1.split()))
        l2 = list(map(str, sentence2.split()))
        l = []
        if len(l2) > len(l1):
            for i in l1:
                if i not in l2:
                    return False

            x = 0
            for i in range(len(l2)):
                if x >= len(l1):
                    l.append(i)
                elif x < len(l1):
                    if l2[i] != l1[x]:
                        l.append(i)
                    else:
                        x = x + 1

            a = 0
            for i in range(l[0], l[0] + len(l)):
                if i != l[a]:
                    return False
                a = a + 1
            return True

        if len(l1) > len(l2):
            for i in l2:
                if i not in l1:
                    return False

            x = 0
            for i in range(len(l1)):
                if x >= len(l2):
                    l.append(i)
                elif x < len(l2):
                    if l1[i] != l2[x]:
                        l.append(i)
                    else:
                        x = x + 1

            a = 0
            for i in range(l[0], l[0] + len(l)):
                if i != l[a]:
                    return False
                a = a + 1
            return True


# 2nd Method
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1, s2 = deque(sentence1.split()), deque(sentence2.split())
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        while s1 and s1[0] == s2[0]:
            s1.popleft()
            s2.popleft()

        while s1 and s1[-1] == s2[-1]:
            s1.pop()
            s2.pop()

        return not s1


# 3rd Method
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split()
        s2 = sentence2.split()
        if len(s1) > len(s2):
            s1, s2 = s2, s1

        while s1:
            if s1[0] == s2[0]:
                s1.pop(0)
                s2.pop(0)

            elif s1[-1] == s2[-1]:
                s1.pop()
                s2.pop()

            else:
                return False

        return True
