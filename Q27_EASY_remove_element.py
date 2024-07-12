from typing import List

## My Solution
def removeElement(nums: List[int], val: int) -> int:
    """My Code"""

    if len(nums) == 0:
        return 0

    left = 0
    right = 0
    size = len(nums)
    count = 0

    for num in nums:
        if num != val:
            count += 1

    while left < size:
        if nums[left] == val:
            break
        left += 1
        right += 1

    while right < size:
        if nums[right] == val:
            right += 1
        else:
            nums[left] = nums[right]
            right += 1
            left += 1

    return count

# Easy Elegant Solution
# slow pointer - fast pointer. Move fast. Only copy to slow if fast != val
def removeElement_Elegent(nums: List[int], val: int) -> int:
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i

print(removeElement_Elegent(nums=[1, 2, 2, 1], val=1))
print(removeElement(nums=[1, 2, 2, 1], val=2))
print(removeElement(nums=[1, 1, 1, 2, 2], val=2))
print(removeElement(nums=[1, 1, 1, 2, 2], val=1))
print(removeElement(nums=[1], val=1))
print(removeElement(nums=[1], val=2))
print(removeElement(nums=[3, 2, 2, 3], val=3))
print(removeElement(nums=[], val=1))
