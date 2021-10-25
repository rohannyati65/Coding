# 315. Count of Smaller Numbers After Self (leetcode)
# 1st Attempt (2 pointer approach , TLE)
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return [0]
        l = []
        left = 0
        right = 1
        count = 0
        while left < right:
            # print(left,right)
            if right == len(nums) - 1:
                if left == (len(nums) - 2):
                    if nums[left] > nums[right]:
                        l.append(1)
                    else:
                        l.append(0)
                    break
                else:
                    if nums[left] > nums[right]:
                        count += 1

                    l.append(count)
                    left = left + 1
                    right = left + 1
                    count = 0
            else:
                if nums[left] > nums[right]:
                    count += 1
                right = right + 1

        l.append(0)
        return l


# 2nd Attempt
