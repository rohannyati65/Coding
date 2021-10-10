# 220. Contains Duplicate III (leetcode)
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:

        if t == 0 and len(set(nums)) == len(nums):

            # Quick response for t = 0
            # t = 0 requires at least one pair of repeated element

            return False

        size = len(nums)

        bucket = {}

        width = t + 1

        for idx, number in enumerate(nums):

            bucket_idx = number // width

            if bucket_idx in bucket:

                # two numbers in the same bucket, gap must be smaller than width
                return True

            elif (
                bucket_idx + 1 in bucket
                and abs(number - bucket[bucket_idx + 1]) < width
            ):

                # two number in two consecutive buckets, and gap is smaller than width
                return True

            elif (
                bucket_idx - 1 in bucket
                and abs(number - bucket[bucket_idx - 1]) < width
            ):

                # two number in two consecutive buckets, and gap is smaller than width
                return True

            # put current number into corresponding bucket
            bucket[bucket_idx] = number

            if idx >= k:

                # delete old number whose index distance larger than k
                del bucket[nums[idx - k] // width]

        return False
