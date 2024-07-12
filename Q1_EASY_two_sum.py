from typing import List

# My version.
# I am setting a list as the value of the dictionary.
def twoSumV2(nums: List[int], target: int) -> List[int]:
    index_map = {}
    # Set indexes against value
    for i in range(len(nums)):
        index_map.setdefault(nums[i], [])
        index_map[nums[i]].append(i)

    # Get the pair
    for i in range(len(nums)):
        remainder = target - nums[i]
        if remainder in index_map:
            remindexes = index_map[remainder]
            for j in range(len(remindexes)):
                if(i != remindexes[j]):
                    return [i, remindexes[j]]
    return []

# Optimized solution
# We don't need the list. if duplicate values exist, just having one index recorded is enough.
def twoSum( nums: List[int], target: int) -> List[int]:
    numbers = {}
    for i in range(len(nums)):
        numbers[nums[i]] = i
    for i in range(len(nums)):
        if target - nums[i] in numbers and numbers[target - nums[i]] != i:
            return [i, numbers[target - nums[i]]]
    return []
