import sys
from typing import List


class Solution:

    ## O(nlogn) solution
    ## Intuition:
    ## - Sort the array
    ## - Then send i from 1 to end. If its incrementing, add to count.
    ## This is not the best solution. Check below
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        count = 1
        max_count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i-1] + 1:
                    count += 1
                else:
                    max_count = max(count, max_count)
                    count = 1
        return max(count, max_count)


    def longestConsecutiveBest(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        longest = curr = 0

        for i in unique_nums:
            # Check the lowest most point to start consecutive check.
            if i - 1 not in unique_nums:
                curr = 1
                while(i + 1 in unique_nums):
                    curr += 1
                    i += 1
            longest = max(curr, longest)
        return longest