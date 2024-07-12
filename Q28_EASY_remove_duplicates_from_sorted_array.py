from typing import List

# Intuition: 0th index is alway unique. So fixing from index 1
# If two adjacent values [0,1] or [1,2] are equal, they are distinct so we can copy.
# If they are equal, keep moving forward to find a unique one.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insert_idx = 1
        for j in range(1, len(nums)):
            # First time I am seeing this number. I should add it
            if(nums[j] != nums[j - 1]):
                nums[insert_idx] = nums[j]
                insert_idx += 1
        return insert_idx

print(Solution().removeDuplicates([1, 2, 4, 4, 4]))
print(Solution().removeDuplicates([4, 4, 4, 4, 4]))
print(Solution().removeDuplicates([4]))