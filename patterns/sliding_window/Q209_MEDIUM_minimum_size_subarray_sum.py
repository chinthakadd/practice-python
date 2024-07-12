import sys
from typing import List

class Solution:

    # This is a sliding window problem.
    # No sorting : coz we are looking for a sub-array -> Contiguous.
    # Sliding window works without any issue.
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if nums[0] >= target: return 1

        i = 0
        sum = nums[i]
        # res = float('inf') can be used.
        min_len = sys.maxsize

        for j in range(1, len(nums)):
            sum += nums[j]
            while sum >= target and j > i:
                min_len = min(min_len, j - i + 1)
                sum -= nums[i]
                i += 1
            if sum >= target:
                min_len = min(min_len, j - i + 1)
        return 0 if min_len == sys.maxsize else min_len

    def minSubArrayLen2(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        sumOfCurrentWindow = 0
        res = float('inf')

        for right in range(0, len(nums)):
            sumOfCurrentWindow += nums[right]

            while sumOfCurrentWindow >= target:
                res = min(res, right - left + 1)
                sumOfCurrentWindow -= nums[left]
                left += 1

        return res if res != float('inf') else 0

print(Solution().minSubArrayLen(213, [12,28,83,4,25,26,25,2,25,25,25,12]))