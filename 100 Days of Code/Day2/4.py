# Sort a stack  (gfg)


class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def sorted(self, s):
        s.sort()
        s[:] = s[::-1]
        return s
