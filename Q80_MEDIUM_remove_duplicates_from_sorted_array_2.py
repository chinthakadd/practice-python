from typing import List

# Intuition: First refer Q28: Remove Duplicate from Sorted Array 01
# This solution extends on it.
# Compare two adjacent elements starting from index 1. Since index 0 is already unique.
# If adjacent elements are different, we can keep moving forward
# If they are the same, Q28 just skip them. But here, we can allow one duplicate.
# If duplicate is already found, then we skip.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return 1;

        insert_idx = 1
        dup = False

        for i in range(1, len(nums)):
            if (nums[i] != nums[i - 1]):
                nums[insert_idx] = nums[i]
                insert_idx += 1
                dup = False
            else:
                if (not dup):
                    dup = True
                    nums[insert_idx] = nums[i]
                    insert_idx += 1
                # Else we skip.
        return insert_idx
