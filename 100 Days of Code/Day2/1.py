# Unique Email Addresses (leetcode)
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        l = []
        l1 = []
        for i in emails:
            x = i.index("@")
            if i[x + 1 :] == "leetcode.com":
                l.append(i[:x])
            else:
                l1.append(i[x + 1 :])
        # print(l)
        # print(l1)
        count = 0
        if len(l) > 0:
            for i in range(len(l)):
                if "+" in l[i]:
                    a = l[i].index("+")
                    l[i] = l[i][:a]

                if "." in l[i]:
                    l[i] = l[i].replace(".", "")
                    # print(l[i])

            # print(l)
            s = set(l)
            count += len(s)

        if len(l1) > 0:
            for i in range(len(l1)):
                if "." in l1[i]:
                    l1[i] = l1[i].replace(".", "")
                    # print(l1[i])
            # print(l1)
            s1 = set(l1)
            count += len(s1)

        return count
