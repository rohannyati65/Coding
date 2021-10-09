# 347. Top K Frequent Elements (leetcode)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        s = list(set(nums))
        for i in s:
            d[i] = nums.count(i)
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
