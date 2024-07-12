from typing import List


class Solution:
    # Intuition:
    # Simple count map.
    # If a count goes above n / 2, and one of them will, thats the answer.
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        for i in nums:
            counts.setdefault(i, 0)
            counts[i] += 1
            if(counts[i] > len(nums) / 2):
                return i
        return -1

    # Now this is a better solution
    # Boyer-Moore Voting Algorithm
    # Watch Video: https://www.youtube.com/watch?v=gY-I8uQrCkk&t=254s to understand how it works
    def majorityElementBoyerMoore(self, nums: List[int]) -> int:

        ## Start with candidate as 0th index value
        candidate = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if(nums[i] == candidate):
                count += 1
            else:
                count -= 1
                ## When count is zero, pick a new candidate
                if(count == 0):
                    candidate = nums[i]
                    count = 1

        return candidate