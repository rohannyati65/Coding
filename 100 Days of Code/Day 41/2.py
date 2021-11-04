# 482. License Key Formatting (leetcode)

# Here we work with the reverse of the given string after removing all '-' .

# We do so since we are given that the first groups length can be less
# than or equal to the value of k .

# So we add strings of length k and then add the remaining string at its
# end , so that when we reverse the output we get the correct output .


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper()
        s = s.replace("-", "")

        if len(s) < k:
            return s

        x = s[::-1]
        z = len(x) // k
        y = ""
        a = 0
        while z != 0:
            y = y + x[a : a + k]
            a = a + k
            z = z - 1
            if z != 0:
                y = y + "-"

        if a != len(x):
            y = y + "-" + x[a:]

        return y[::-1]
