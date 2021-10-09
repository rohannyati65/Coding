# 692. Top K Frequent Words (leetcode)
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        s = list(set(words))
        for i in s:
            d[i] = words.count(i)
        r = sorted(d.items(), key=lambda x: (-x[1], x[0]))
        # print(d)
        # print(r)
        l = []
        for i in range(k):
            l.append(r[i][0])

        return l
        # words.sort(key=count,reverse=True)
        # result = sorted(d, key = d.value)
        # print(list(set(result)))
        # for i in range(k):
