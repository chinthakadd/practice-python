from typing import List


def duplicateZeros(arr: List[int]) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """
    dup_count = 0
    original_len = len(arr)
    idx = 0
    while idx < original_len - dup_count:
        if arr[idx] == 0:
            # Edge case: This zero can't be duplicated. We have no more space,
            # as left is pointing to the last element which could be included
            if idx == (original_len - dup_count - 1):
                arr[original_len - 1] = 0
                original_len -= 1
            else:
                dup_count += 1
        idx += 1

    copy_idx = original_len - dup_count - 1

    while copy_idx >= 0:
        arr[original_len - 1] = arr[copy_idx]
        original_len -= 1
        if arr[copy_idx] == 0:
            arr[original_len - 1] = 0
            original_len -= 1
        copy_idx -= 1


sample_arr = [1, 0, 0, 1, 1, 0]
duplicateZeros(arr=sample_arr)
print(sample_arr)

sample_arr2 = [1, 0, 0, 0, 1, 0]
duplicateZeros(arr=sample_arr2)
print(sample_arr2)