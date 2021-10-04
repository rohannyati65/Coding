# Merge k Sorted Arrays (gfg)


class Solution:
    # Function to merge k sorted arrays.
    def mergeKArrays(self, arr, K):
        l = []
        for i in arr:
            l = l + i
        l.sort()
        return l
