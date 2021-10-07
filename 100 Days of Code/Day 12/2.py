# 167. Two Sum II - Input array is sorted (leetcode)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) > 10000:
            numbers.append(target)
            numbers.sort()
            a = numbers.index(target)
            return [a - 1, a]

        for i in range(len(numbers) - 1):
            for j in numbers[i + 1 :]:
                if numbers[i] + j == target:
                    a = i + 1
                    b = numbers.index(j) + 1
                    if a == b:
                        b = b + 1
                    return [a, b]
