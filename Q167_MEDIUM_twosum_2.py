from typing import List

# Wrote with recursion
class Solution:
    def twoSumRec(self, numbers: List[int], left: int, right: int, target: int) -> List[int]:
        leftval = numbers[left]
        rightval = numbers[right]
        if(leftval + rightval > target):
            return self.twoSumRec(numbers, left, right - 1, target)
        elif(leftval + rightval < target):
            return self.twoSumRec(numbers, left + 1, right, target)
        else: return [left + 1, right + 1]

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        return self.twoSumRec(numbers, 0, len(numbers) - 1, target)

print(Solution().twoSum([1,2,3], 4))