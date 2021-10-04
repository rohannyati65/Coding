# 1143. Longest Common Subsequence  (leetcode)

# 1st attempt
import itertools


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == text2:
            return len(text1)

        l3 = [i for i in text1]
        l1 = [l3]
        for i in range(1, len(text1)):
            l = list(map(list, itertools.combinations(text1, i)))
            l1 = l1 + l
        l1.sort(key=len)
        l1[:] = l1[::-1]

        l3 = [i for i in text2]
        l2 = [l3]
        for i in range(1, len(text2)):
            l = list(map(list, itertools.combinations(text2, i)))
            l2 = l2 + l
        l2.sort(key=len)
        l2[:] = l2[::-1]

        if len(text1) >= len(text2):
            for i in l2:
                if i in l1:
                    return len(i)

        if len(text1) < len(text2):
            for i in l1:
                if i in l2:
                    return len(i)

        return 0


# 2nd attempt


class Solution:
    def longestCommonSubsequence(self, text1, text2):
        text1 = "!" + text1
        text2 = "!" + text2
        m, n = len(text1), len(text2)
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i, j in product(range(m), range(n)):
            if text1[i] == text2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1] - 1
