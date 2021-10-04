# Rearrange an array with O(1) extra space  (gfg)


class Solution:
    # Function to rearrange an array so that arr[i] becomes arr[arr[i]]
    # with O(1) extra space.
    def arrange(self, arr, n):
        for i in range(len(arr)):
            a = arr[i]
            b = arr[a]
            arr.insert(n + i, b)
        arr[:] = arr[n:]
        return arr
